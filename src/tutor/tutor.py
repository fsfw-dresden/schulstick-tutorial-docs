from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRect, QUrl
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from pathlib import Path
from typing import Optional
from core.models import ScreenHint, UnitMetadata

class TutorView(QWidget):
    def __init__(self, unit: UnitMetadata):
        super().__init__()
        self.unit = unit
        self.screen_hint = unit.screen_hint or ScreenHint(position="right", mode="docked")
        self.is_expanded = True  # Start in expanded state
        
        # Set window properties
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Get current screen based on mouse position
        cursor_pos = QApplication.desktop().cursor().pos()
        self.current_screen = QApplication.desktop().screenNumber(cursor_pos)
        
        # Initialize screen geometry and apply hints
        self.update_screen_geometry()
        self.apply_screen_hints()

    def update_screen_geometry(self):
        """Update geometry based on current screen"""
        screen = QApplication.desktop().screenGeometry(self.current_screen)
        self.screen_width = screen.width()
        self.screen_height = screen.height()
        self.screen_x = screen.x()
        self.screen_y = screen.y()
        
        # Create layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 0, 0, 0)
        
        # Create web view with transparent background
        self.web_view = QWebEngineView(self)
        self.web_view.page().setBackgroundColor(Qt.transparent)
        
        if self.unit.tutorial_url:
            self.load_tutorial(self.unit.tutorial_url)
            
        self.layout.addWidget(self.web_view)
        
        # Create toggle button
        self.toggle_btn = QPushButton("◀", self)
        self.toggle_btn.setFixedSize(20, 60)
        self.toggle_btn.clicked.connect(self.toggle_expansion)
        self.toggle_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(60, 60, 60, 200);
                border: none;
                border-radius: 5px;
                color: white;
            }
            QPushButton:hover {
                background-color: rgba(80, 80, 80, 200);
            }
        """)
        self.update_button_position()
        
        # Setup animation
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)

    def apply_screen_hints(self):
        """Apply screen positioning hints"""
        # Set default dimensions
        self.expanded_width = self.screen_width // 3
        self.collapsed_width = 30
        
        # Apply size hints if provided
        if self.screen_hint.preferred_width:
            self.expanded_width = min(self.screen_hint.preferred_width, self.screen_width)
            
        if self.screen_hint.preferred_height:
            height = min(self.screen_hint.preferred_height, self.screen_height)
            self.setFixedHeight(height)
        else:
            self.setFixedHeight(self.screen_height)
            
        # Calculate height based on aspect ratio if provided
        if self.screen_hint.preferred_aspect and not (self.screen_hint.preferred_width and self.screen_hint.preferred_height):
            if self.screen_hint.preferred_width:
                height = int(self.screen_hint.preferred_width / self.screen_hint.preferred_aspect)
                self.setFixedHeight(min(height, self.screen_height))
            elif self.screen_hint.preferred_height:
                width = int(self.screen_hint.preferred_height * self.screen_hint.preferred_aspect)
                self.expanded_width = min(width, self.screen_width)
        
        # Position window based on screen hint position
        if self.screen_hint.position == "top":
            self.setGeometry(
                self.screen_x + (self.screen_width - self.expanded_width) // 2,
                self.screen_y,
                self.expanded_width,
                self.height()
            )
        elif self.screen_hint.position == "bottom":
            self.setGeometry(
                self.screen_x + (self.screen_width - self.expanded_width) // 2,
                self.screen_y + self.screen_height - self.height(),
                self.expanded_width,
                self.height()
            )
        elif self.screen_hint.position == "left":
            self.setGeometry(
                self.screen_x,
                self.screen_y + (self.screen_height - self.height()) // 2,
                self.expanded_width,
                self.height()
            )
        else:  # Default to right if no position or position is "right"
            self.setGeometry(
                self.screen_x + self.screen_width - self.expanded_width,
                self.screen_y,
                self.expanded_width,
                self.height()
            )

    def load_tutorial(self, url: str):
        """Load a tutorial from a URL"""
        self.web_view.load(QUrl(url))
        
    def update_button_position(self):
        """Update toggle button position based on expansion state"""
        self.toggle_btn.move(0, self.height() // 2 - 30)
        self.toggle_btn.setText("▶" if self.is_expanded else "◀")
        
    def toggle_expansion(self):
        """Toggle between expanded and collapsed states"""
        self.is_expanded = not self.is_expanded
        
        new_width = self.expanded_width if self.is_expanded else self.collapsed_width
        new_x = self.screen_width - new_width
        
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(QRect(
            new_x,
            self.y(),
            new_width,
            self.height()
        ))
        
        self.animation.start()
        self.update_button_position()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Draw semi-transparent background
        painter.fillRect(self.rect(), QColor(40, 40, 40, 200))
