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
        self.setFixedSize(300, 350)  # Set fixed size for all cards
        self.setStyleSheet("""
            QFrame {
                background-color: #2d2d2d;
                border-radius: 8px;
                padding: 12px;
                border: 1px solid #3d3d3d;
            }
            QLabel#title {
                font-size: 16px;
                font-weight: bold;
                color: white;
                margin-top: 8px;
            }
            QLabel#tag {
                background-color: #454545;
                color: #e0e0e0;
                border-radius: 4px;
                padding: 2px 6px;
            }
            QLabel#skill {
                color: #b0b0b0;
                margin: 4px 0;
            }
        """)
        
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout(self)
        
        # Preview image
        preview = QLabel()
        pixmap = QPixmap(str(self.unit.preview_path))
        preview.setPixmap(pixmap.scaled(276, 180, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        preview.setAlignment(Qt.AlignCenter)
        layout.addWidget(preview)
        
        # Title
        title = QLabel(self.unit.title)
        title.setObjectName("title")
        title.setWordWrap(True)
        layout.addWidget(title)
        
        # Skill level
        skill_info = QLabel(f"Skill Level: {self.unit.skill_level}/5")
        skill_info.setObjectName("skill")
        layout.addWidget(skill_info)
        
        # Tags
        tags_layout = QHBoxLayout()
        for tag in self.unit.tags[:3]:  # Show first 3 tags
            tag_label = QLabel(tag)
            tag_label.setObjectName("tag")
            tags_layout.addWidget(tag_label)
        tags_layout.addStretch()
        layout.addLayout(tags_layout)
