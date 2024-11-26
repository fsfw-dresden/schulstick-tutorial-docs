from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, 
                            QHBoxLayout, QFrame, QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from core.unit_scanner import UnitMetadata

class UnitCard(QFrame):
    def __init__(self, unit: UnitMetadata, parent=None):
        super().__init__(parent)
        self.unit = unit
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 8px;
                padding: 8px;
            }
            QLabel#title {
                font-size: 16px;
                font-weight: bold;
            }
            QLabel#tag {
                background-color: #e0e0e0;
                border-radius: 4px;
                padding: 2px 6px;
            }
        """)
        
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout(self)
        
        # Preview image
        preview = QLabel()
        pixmap = QPixmap(str(self.unit.preview_path))
        preview.setPixmap(pixmap.scaled(200, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        preview.setAlignment(Qt.AlignCenter)
        layout.addWidget(preview)
        
        # Title
        title = QLabel(self.unit.title)
        title.setObjectName("title")
        title.setWordWrap(True)
        layout.addWidget(title)
        
        # Skill level
        skill_info = QLabel(f"Skill Level: {self.unit.skill_level}/5")
        layout.addWidget(skill_info)
        
        # Tags
        tags_layout = QHBoxLayout()
        for tag in self.unit.tags[:3]:  # Show first 3 tags
            tag_label = QLabel(tag)
            tag_label.setObjectName("tag")
            tags_layout.addWidget(tag_label)
        tags_layout.addStretch()
        layout.addLayout(tags_layout)
