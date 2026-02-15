from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional, List
from datetime import datetime, timezone, timedelta
import hashlib
import json
import math

import pandas as pd
import numpy as np


# ----------------------------
# 1) Pseudonymous user id
# ----------------------------
def pseudonymous_id(external_user_id: str, salt: str) -> str:
    """
    external_user_id: email/phone/internal id (đừng log thẳng cái này)
    salt: giữ trong secret manager / env var
    """
    h = hashlib.sha256((salt + external_user_id).encode("utf-8")).hexdigest()
    return f"u_{h[:24]}"


# ----------------------------
# 2) Event schema
# ----------------------------
@dataclass
class Event:
    ts: datetime
    user_pid: str
    name: str
    props: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["ts"] = self.ts.replace(tzinfo=timezone.utc).isoformat()
        return d


# ----------------------------
# 3) Ingest: append-only log (file/db/kafka)
# ----------------------------
def append_event(event: Event, path: str = "events.jsonl") -> None:
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(event.to_dict(), ensure_ascii=False) + "\n")


def load_events(path: str = "events.jsonl") -> pd.DataFrame:
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    df = pd.DataFrame(rows)
    df["ts"] = pd.to_datetime(df["ts"], utc=True)
    return df


# ----------------------------
# 4) Feature builder
# ----------------------------
def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def build_user_features(
    df: pd.DataFrame,
    now: Optional[pd.Timestamp] = None,
    window_days: int = 7,
) -> pd.DataFrame:
    """
    Input df columns: ts, user_pid, name, props(dict)
    Output: per-user features for analytics + recommender
    """
    if now is None:
        now = pd.Timestamp.now(tz="UTC")
    start = now - pd.Timedelta(days=window_days)

    dfw = df[df["ts"] >= start].copy()
    if dfw.empty:
        return pd.DataFrame(columns=["user_pid"])

    # explode props fields we care about
    def get_prop(d, k, default=0):
        if isinstance(d, dict) and k in d:
            return d[k]
        return default

    dfw["minutes"] = dfw["props"].apply(lambda d: get_prop(d, "minutes", 0))
    dfw["seconds_watched"] = dfw["props"].apply(lambda d: get_prop(d, "seconds_watched", 0))
    dfw["completed"] = (dfw["name"] == "content_completed").astype(int)
    dfw["quiz_attempt"] = (dfw["name"] == "quiz_attempt").astype(int)
    dfw["quiz_score"] = dfw["props"].apply(lambda d: get_prop(d, "score", np.nan))
    dfw["quiz_max"] = dfw["props"].apply(lambda d: get_prop(d, "max", np.nan))
    dfw["note"] = (dfw["name"] == "note_created").astype(int)

    # active days
    dfw["day"] = dfw["ts"].dt.floor("D")

    g = dfw.groupby("user_pid")
    agg = pd.DataFrame({
        "minutes": g["minutes"].sum(),
        "seconds_watched": g["seconds_watched"].sum(),
        "active_days": g["day"].nunique(),
        "completions": g["completed"].sum(),
        "quiz_attempts": g["quiz_attempt"].sum(),
        "notes": g["note"].sum(),
        "last_ts": g["ts"].max(),
    }).reset_index()

    agg["days_since_last"] = (now - agg["last_ts"]).dt.total_seconds() / 86400.0

    # quiz accuracy (safe: ignore if missing)
    qa = dfw[dfw["name"] == "quiz_attempt"].copy()
    if not qa.empty:
        qa["accuracy"] = np.where(
            (qa["quiz_max"] > 0) & (~qa["quiz_score"].isna()),
            qa["quiz_score"] / qa["quiz_max"],
            np.nan
        )
        acc = qa.groupby("user_pid")["accuracy"].mean().rename("quiz_accuracy")
        agg = agg.merge(acc, on="user_pid", how="left")
    else:
        agg["quiz_accuracy"] = np.nan

    # Engagement score
    w1, w2, w3, w4, w5 = 0.9, 0.7, 0.8, _0.6, 0.4
    z = (
        w1 * np.log1p(agg["minutes"]) +
        w2 * agg["active_days"] +
        w3 * agg["completions"] +
        w4 * agg["quiz_attempts"] +
        w5 * agg["notes"]
    )
    agg["engagement_score"] = (100.0 * z.apply(sigmoid)).clip(0, 100)

    # Simple churn risk (0..1)
    completion_rate_approx = (agg["completions"] / (agg["active_days"].clip(lower=1))).clip(0, 1)
    R = (
        0.55 * (agg["days_since_last"].clip(0, 30) / 30.0) +
        0.25 * (1.0 - (agg["active_days"].clip(0, window_days) / window_days)) +
        0.20 * (1.0 - completion_rate_approx)
    )
    agg["churn_risk"] = R.clip(0, 1)

    return agg


# ----------------------------
# 5) Topic mastery (EMA per user-topic)
# ----------------------------
def update_mastery_ema(
    mastery_prev: float,
    quiz_accuracy: float,
    alpha: float = 0.3
) -> float:
    if np.isnan(quiz_accuracy):
        return mastery_prev
    return float(alpha * quiz_accuracy + (1 - alpha) * mastery_prev)


# ----------------------------
# 6) Recommendation hook (rule-based starter)
# ----------------------------
def recommend_next_action(user_row: pd.Series) -> Dict[str, Any]:
    """
    Output is a structured plan for your AI agent to execute:
    - message style
    - suggested content type
    - urgency
    """
    churn = float(user_row.get("churn_risk", 0))
    eng = float(user_row.get("engagement_score", 0))
    acc = user_row.get("quiz_accuracy", np.nan)

    if churn > 0.7:
        return {
            "priority": "high",
            "action": "nudge_short",
            "content": "short_lesson_or_recap",
            "message": "Nhắc nhẹ + 1 bài ngắn 5–8 phút để lấy lại nhịp."
        }

    if (not np.isnan(acc)) and acc < 0.55 and eng >= 50:
        return {
            "priority": "medium",
            "action": "scaffold",
            "content": "foundation_lesson",
            "message": "Đề xuất bài nền tảng + quiz ngắn để củng cố."
        }

    if eng >= 80:
        return {
            "priority": "low",
            "action": "deepen",
            "content": "advanced_or_project",
            "message": "Đề xuất bài nâng cao / bài tập dự án / hoạt động cộng đồng."
        }

    return {
        "priority": "low",
        "action": "steady",
        "content": "next_in_path",
        "message": "Gợi ý bài tiếp theo đúng lộ trình."
    }
