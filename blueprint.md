# Blueprint: Noi App

## Overview

This document outlines the architecture and implementation plan for the Noi learning application, including a sophisticated analytics and personalization engine and a Gemini-powered chatbot.

## Architecture

- **Client-Side (Browser)**: A single-page application (`index.html`) built with Vanilla JavaScript and Tailwind CSS. Its primary responsibilities are rendering the UI, capturing user behavior events, and providing the chatbot interface.
- **Backend (Server-Side)**: A Python-based analytics engine (`analytics_engine.py`) responsible for processing raw event data, calculating user features, and providing recommendation logic.

## 1. Client-Side Features

### 1.1. Gemini-Powered Chat & Search

**Objective**: Replace the static search bar on the Home screen with an interactive entry point to a Gemini-powered chatbot, creating a seamless and intelligent user support experience.

**Implementation**:

1.  **UI Transformation**: The search bar in `renderHome()` will be restyled into a chat prompt, featuring an icon and inviting text (e.g., "Trò chuyện cùng AI Nhi Le...").
2.  **Modal Integration**: Clicking this new search bar will trigger the `app.toggleAIChat()` function, opening a full-screen chat modal (`ai-modal`).
3.  **Contextual Hand-off**: Any text the user types into the search bar will be passed as the initial message in the chat window.
4.  **Chat Logic**: The `toggleAIChat`, `sendMessage`, and `addMessageToHistory` functions will be fully implemented to manage the chat session's state, display messages, and simulate AI responses.

### 1.2. Behavior Tracking

**Objective**: Capture user interactions for backend analysis.

**Implementation**:

-   **`app.trackEvent(name, props)`**: A core JS function logs events to the console, simulating a backend data pipeline. Events include `session_start`, `content_impression`, `content_open`, `topic_select`, and `search_initiated`.
-   **Pseudonymous ID**: A `user_pid` is generated on sign-in to ensure privacy.

## 2. Backend: Analytics Engine (`analytics_engine.py`)

**Objective**: Process event data to generate actionable insights.

This engine contains the Python code for:
-   **Feature Engineering**: Calculates `engagement_score` and `churn_risk`.
-   **Mastery Model**: Uses an EMA to track topic proficiency.
-   **Recommendation Policy**: A rule-based system (`recommend_next_action`) to suggest actions for the AI agent based on user features.
