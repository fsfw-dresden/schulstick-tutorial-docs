# 0.1.2 (2024-11-28)

## Summary

Mainly work on TutorView. Improve link handling and different view modes and orientation. Also added a release script
and a x11docker method to test application under debian bookworm.

## Features

- Added German translations for external link dialog strings
- Implemented external link handling with user preferences and `xdg-open` support
- Added external link click detection and logging in the WebEngine view
- Persisted the current URL when changing view modes in the TutorView
- Added a Dockerfile for an XFCE desktop environment
- Added context menu support for the web view in free mode
- Enabled native window decorations in free floating mode
- Implemented flexible Tutor View with dynamic orientation and mode handling

## Fixes

- Improved JavaScript message handling and URL change detection
- Resolved a reference error by dynamically loading the QWebChannel library
- Implemented web channel message handling for hash state changes
- Improved JavaScript message handling and URL change detection

## Other Changes

- Refactored translation handling for multiple packages
- Removed unused imports and simplify page load handling
- Enhanced JavaScript message handling with detailed logging and error handling
