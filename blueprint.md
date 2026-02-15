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

*   **Application UI**: A comprehensive user interface for a community platform, including authentication, navigation, user profiles, content feeds, and an AI chat modal.
*   **Google Analytics**: Integrated Google Analytics 4 using the standard `gtag.js` script in `index.html` to track user activity.
*   **Deployment Fixes**: Corrected the build process to handle a vanilla JS project instead of a React-based one.

## Current Plan: Collapsible Navigation Menu

**Objective**: Implement a modern, collapsible sidebar navigation menu similar to the Gemini UI to create a cleaner and more organized interface.

**Steps**:

1.  **Create Menu Icon**: Add a "hamburger" menu icon to the top-left corner of the main application view.
2.  **Build Sidebar Panel**: Construct a sidebar container that will be hidden by default and will slide in from the left.
3.  **Relocate Navigation**: Move the existing primary navigation links ("Trang chủ", "Học tập", "Cộng đồng", "Nhiệm vụ") into the new sidebar.
4.  **Implement Logic**: Write JavaScript functions to toggle the sidebar's visibility with a smooth slide-in/slide-out animation.
5.  **Refine Styling**: Ensure the sidebar and menu icon are styled to match the application's modern aesthetic and are fully responsive.
