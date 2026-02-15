# Blueprint: Noi App

## Overview

This project is a modern React application built with Vite. It's designed to be a simple, clean, and interactive user interface. The application is deployed to Cloudflare Pages.

## Project Documentation

### Core Technologies

*   **Framework**: React (with Vite)
*   **Language**: JavaScript (JSX)
*   **Package Manager**: npm
*   **Styling**: Plain CSS (initially)
*   **Deployment**: Cloudflare Pages via Wrangler CLI

### Features Implemented

*   **Initial Scaffolding**: Standard Vite + React project setup.
*   **Deployment Configuration**:
    *   Added `_redirects` for client-side routing on Cloudflare Pages.
    *   Configured `.gitignore` to exclude build artifacts (`dist`) and dependencies (`node_modules`).
    *   Created `wrangler.toml` for simplified deployment via the Wrangler CLI.

## Current Plan

**Objective**: Finalize the project setup for manual deployment.

**Steps**:

1.  **DONE**: Create `wrangler.toml` to configure Cloudflare Pages deployment.
2.  **CURRENT**: Commit `wrangler.toml` and the initial `blueprint.md` to the Git repository.
3.  **NEXT**: The project is now ready for a streamlined manual deployment workflow using `npm run build` and `npx wrangler pages deploy`.
