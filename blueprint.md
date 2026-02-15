# Blueprint: Noi App

## Overview

This project is a single-page application built with vanilla HTML, CSS, and JavaScript, designed as an interactive community hub.

## Project Documentation

### Core Technologies

*   **Structure**: Single HTML file (`index.html`)
*   **Logic**: Vanilla JavaScript
*   **Styling**: Tailwind CSS (via CDN)

### Features Implemented

*   **Full UI Suite**: Authentication, Sidebar Navigation, Home, Community, Live, Profile pages.
*   **Course Detail View**: Users can click on a course to see its detailed contents, including a lesson list.
*   **State Management**: A global `store` object manages the application's state, including the current view (`currentView`).
*   **Dynamic Rendering**: A central `app.render()` function that displays content based on the `store.currentView`.

## Current Plan: Activate Category Filters

**Objective**: Allow users to filter the course list by clicking on the category buttons on the "Học tập" screen.

**Steps**:

1.  **Create New View State**: Introduce a new view state, `category_page`, to represent the filtered course list screen.
2.  **Create `renderCategoryPage` Function**: This function will:
    *   Take a `categoryName` as an argument.
    *   Filter the `store.roadmap` array to find all courses matching the category.
    *   Generate HTML to display the list of filtered courses, reusing the existing card component style.
3.  **Update Navigation Logic**: 
    *   Modify the `app.navigate` function to accept an optional `data` payload (e.g., `{ categoryName: 'Tâm lý' }`).
    *   Add a case for `category_page` in the main `render()` switch statement.
    *   Update `renderHeader` to display the category name as the title and show a 'Back' button to return to the `home` view.
4.  **Add `onclick` Events**: Attach `onclick` events to the category buttons in the `renderHome` function to call `app.navigate('category_page', { categoryName: '...' })`.
