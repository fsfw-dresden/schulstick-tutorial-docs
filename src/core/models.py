from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List
from dataclass_wizard import YAMLWizard

@dataclass
class UnitMetadata(YAMLWizard):
    title: str
    tags: List[str]
    min_grade: int
    skill_level: int
    subjects: List[str]
    skill_level_per_subject: Dict[str, int]
    markdown_file: str
    preview_image: str
    unit_path: Path = None
    
    @property
    def markdown_path(self) -> Path:
        return self.unit_path / self.markdown_file
    
    @property
    def preview_path(self) -> Path:
        return self.unit_path / self.preview_image
