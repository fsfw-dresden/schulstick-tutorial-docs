# 0.1.2 (2024-11-28)

## Summary

Mainly work on TutorView and configuration system improvements. Added configuration management, unit scanning enhancements,
and LiaScript integration. Also improved link handling, view modes, and orientation support.

## Features

- Added configuration system with environment-aware loading and default settings
- Implemented config system using dataclass_wizard for YAML serialization
- Added program launcher and auto-launch functionality for units
- Added metadata.yml for beginner Blender tutorial
- Enhanced release script functionality
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

- Refactored UnitScanner to use config for scanning unit paths
- Moved LiaScript configuration from hardcoded constants to PortalConfig
- Added LiaScript URL generation and ProgramLaunchInfo to UnitMetadata
- Refactored translation handling for multiple packages
- Removed unused imports and simplify page load handling
- Enhanced JavaScript message handling with detailed logging and error handling
- Fixed DE build pipeline
