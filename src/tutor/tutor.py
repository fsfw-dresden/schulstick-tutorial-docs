from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRect, QUrl
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from pathlib import Path

class TutorView(QWidget):
    def __init__(self, tutorial_url: str = None):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Get current screen based on mouse position
        cursor_pos = QApplication.desktop().cursor().pos()
        self.current_screen = QApplication.desktop().screenNumber(cursor_pos)
        
        # Initialize screen geometry
        screen = QApplication.desktop().screenGeometry(self.current_screen)
        self.screen_width = screen.width()
        self.screen_height = screen.height()
        self.screen_x = screen.x()
        self.screen_y = screen.y()
        
        # Calculate dimensions
        self.expanded_width = self.screen_width // 3
        self.collapsed_width = 30
        self.is_expanded = True
        
        # Position window on right side of current screen
        self.setGeometry(
            self.screen_x + self.screen_width - self.expanded_width,
            self.screen_y,
            self.expanded_width,
            self.screen_height
        )
        
        # Create layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 0, 0, 0)
        
        # Create web view with transparent background
        self.web_view = QWebEngineView(self)
        self.web_view.page().setBackgroundColor(Qt.transparent)
        
        if tutorial_url:
            self.load_tutorial(tutorial_url)
            
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
