# Blueprint: Noi App

## Overview

This project is a single-page application built with vanilla HTML, CSS, and JavaScript. It's designed as an interactive community hub. The application is deployed as a **Cloudflare Worker Site**.

## Project Documentation

### Core Technologies

*   **Structure**: Single HTML file (`index.html`)
*   **Logic**: Vanilla JavaScript
*   **Styling**: Tailwind CSS (via CDN)
*   **Deployment**: Cloudflare Worker Site
*   **Analytics**: Google Analytics 4 (via `gtag.js`)

### Features Implemented

*   **Application UI**: A comprehensive user interface for a community platform.
*   **Google Analytics**: Integrated `gtag.js` for analytics.
*   **Collapsible Sidebar**: A modern, responsive navigation menu.

## Current Plan: Course Detail View

**Objective**: Create a detailed view for individual learning nodes (courses/challenges) that users can navigate to from the main "Học tập" screen.

**Steps**:

1.  **Create New View Function**: Develop a new function `renderCourseDetail(node)` to dynamically generate the HTML for the course detail page.
2.  **Design Detail Layout**: The layout will include:
    *   A prominent header with the course icon and title.
    *   A 'Back' button to return to the previous screen.
    *   A detailed description of the course.
    *   A list of individual lessons or modules (using dummy data initially).
    *   A primary call-to-action button, e.g., "Bắt đầu học".
3.  **Implement Navigation Logic**: 
    *   Create a function `app.openCourse(nodeId)` that finds the course data and triggers the rendering of the detail view.
    *   Add an `onclick="app.openCourse(...)"` event to the "Tiếp tục hành trình" card on the home screen.
    *   Update the main `app.render` function to handle a new view state, e.g., `course_detail`.
