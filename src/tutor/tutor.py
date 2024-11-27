from enum import Enum
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRect, QUrl, QSize
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from pathlib import Path
from typing import Optional, Tuple
from core.models import ViewMode, DockPosition, ScreenHint, UnitMetadata

class CollapseIcons:
    BOTTOM = ("▼", "▲")
    TOP = ("▲", "▼")
    LEFT = ("◀", "▶")
    RIGHT = ("▶", "◀")

class TutorView(QWidget):
    def __init__(self, unit: UnitMetadata):
        super().__init__()
        self.unit = unit
        self.screen_hint = unit.screen_hint or ScreenHint(position=DockPosition.RIGHT, mode=ViewMode.DOCKED)
        self.is_expanded = True
        self.position = DockPosition(self.screen_hint.position)
        self.mode = ViewMode(self.screen_hint.mode)
        
        # Set window properties based on mode
        if self.mode == ViewMode.DOCKED:
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
        else:
            self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        
        # Get current screen based on mouse position
        cursor_pos = QApplication.desktop().cursor().pos()
        self.current_screen = QApplication.desktop().screenNumber(cursor_pos)
        
        # Create main layout based on position
        self.main_layout = QHBoxLayout() if self.position in [DockPosition.LEFT, DockPosition.RIGHT] else QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)
        
        # Create content widget
        self.content_widget = QWidget()
        self.content_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.content_layout = QVBoxLayout(self.content_widget)
        if self.screen_hint.mode == ViewMode.DOCKED:
            self.content_layout.setContentsMargins(0, 0, 0, 0)
        else:
            # Set margins to create draggable area
            self.content_layout.setContentsMargins(20, 20, 20, 20)
            
        # Initialize drag position
        self.drag_position = None
        
        # Create web view with transparent background
        self.web_view = QWebEngineView()
        self.web_view.page().setBackgroundColor(Qt.transparent)
        self.content_layout.addWidget(self.web_view)
        
        if self.unit.tutorial_url:
            self.web_view.load(QUrl(self.unit.tutorial_url))
        
        # Create and setup toggle button if in docked mode
        if self.mode == ViewMode.DOCKED:
            self.toggle_btn = QPushButton()
            self.toggle_btn.clicked.connect(self.toggle_expansion)
            self.setup_toggle_button()
            
            # Add widgets to main layout in correct order
            if self.position in [DockPosition.RIGHT, DockPosition.BOTTOM]:
                self.main_layout.addWidget(self.toggle_btn)
                self.main_layout.addWidget(self.content_widget)
            else:
                self.main_layout.addWidget(self.content_widget)
                self.main_layout.addWidget(self.toggle_btn)
        else:
            self.toggle_btn = None
            self.main_layout.addWidget(self.content_widget)
        
        # Initialize screen geometry and apply hints
        self.update_screen_geometry()
        self.apply_screen_hints()

    def setup_toggle_button(self):
        """Setup the toggle button appearance and position"""
        if self.position in [DockPosition.LEFT, DockPosition.RIGHT]:
            self.toggle_btn.setFixedSize(20, 60)
        else:
            self.toggle_btn.setFixedSize(60, 20)
            
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
        self.update_toggle_button_icon()
        
    def update_toggle_button_icon(self):
        """Update toggle button icon based on position and state"""
        if not self.toggle_btn:
            return
            
        icons = getattr(CollapseIcons, self.position.value.upper())
        self.toggle_btn.setText(icons[0] if self.is_expanded else icons[1])
        
    def update_screen_geometry(self):
        """Update geometry based on current screen"""
        screen = QApplication.desktop().screenGeometry(self.current_screen)
        self.screen_width = screen.width()
        self.screen_height = screen.height()
        self.screen_x = screen.x()
        self.screen_y = screen.y()
        
        # Setup animation
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)

    def get_dimensions(self) -> Tuple[int, int]:
        """Calculate dimensions based on mode and hints"""
        if self.mode == ViewMode.FREE:
            width = min(int(self.screen_width * 0.7), self.screen_hint.preferred_width or self.screen_width)
            height = min(int(self.screen_height * 0.4), self.screen_hint.preferred_height or self.screen_height)
        else:
            if self.position in [DockPosition.LEFT, DockPosition.RIGHT]:
                width = min(self.screen_width // 3, self.screen_hint.preferred_width or self.screen_width)
                height = self.screen_height
            else:
                width = self.screen_width
                height = min(self.screen_height // 3, self.screen_hint.preferred_height or self.screen_height)
                
        return width, height
        
    def apply_screen_hints(self):
        """Apply screen positioning hints"""
        width, height = self.get_dimensions()
        self.expanded_size = QSize(width, height)
        
        # Set collapsed size based on orientation
        if self.mode == ViewMode.DOCKED:
            if self.position in [DockPosition.LEFT, DockPosition.RIGHT]:
                self.collapsed_size = QSize(30, height)
            else:
                self.collapsed_size = QSize(width, 30)
        
        # Calculate initial position
        if self.mode == ViewMode.FREE:
            x = self.screen_x + (self.screen_width - width) // 2
            y = self.screen_y + (self.screen_height - height) // 2
        else:
            if self.position == DockPosition.TOP:
                x = self.screen_x
                y = self.screen_y
            elif self.position == DockPosition.BOTTOM:
                x = self.screen_x
                y = self.screen_y + self.screen_height - height
            elif self.position == DockPosition.LEFT:
                x = self.screen_x
                y = self.screen_y
            else:  # RIGHT
                x = self.screen_x + self.screen_width - width
                y = self.screen_y
        
        self.setGeometry(x, y, width, height)

    def toggle_expansion(self):
        """Toggle between expanded and collapsed states"""
        if self.mode != ViewMode.DOCKED:
            return
            
        self.is_expanded = not self.is_expanded
        current_geo = self.geometry()
        
        if self.position in [DockPosition.LEFT, DockPosition.RIGHT]:
            new_width = self.expanded_size.width() if self.is_expanded else self.collapsed_size.width()
            if self.position == DockPosition.RIGHT:
                new_x = self.screen_x + self.screen_width - new_width
                new_rect = QRect(new_x, current_geo.y(), new_width, current_geo.height())
            else:
                new_rect = QRect(self.screen_x, current_geo.y(), new_width, current_geo.height())
        else:
            new_height = self.expanded_size.height() if self.is_expanded else self.collapsed_size.height()
            if self.position == DockPosition.BOTTOM:
                new_y = self.screen_y + self.screen_height - new_height
                new_rect = QRect(current_geo.x(), new_y, current_geo.width(), new_height)
            else:
                new_rect = QRect(current_geo.x(), self.screen_y, current_geo.width(), new_height)
        
        self.animation.setStartValue(current_geo)
        self.animation.setEndValue(new_rect)
        self.animation.start()
        
        self.update_toggle_button_icon()
        
    def paintEvent(self, event):
        if self.mode == ViewMode.DOCKED:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            
            # Draw semi-transparent background
            painter.fillRect(self.rect(), QColor(40, 40, 40, 200))

    def mousePressEvent(self, event):
        """Handle mouse press events for dragging"""
        if event.button() == Qt.LeftButton and self.mode == ViewMode.FREE:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        """Handle mouse move events for dragging"""
        if event.buttons() & Qt.LeftButton and self.drag_position is not None and self.mode == ViewMode.FREE:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        """Handle mouse release events for dragging"""
        if event.button() == Qt.LeftButton:
            self.drag_position = None
            event.accept()
