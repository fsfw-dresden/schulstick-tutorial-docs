from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional
import yaml
from fuzzywuzzy import fuzz

@dataclass
class UnitMetadata:
    title: str
    tags: List[str]
    min_grade: int
    skill_level: int
    subjects: List[str]
    skill_level_per_subject: Dict[str, int]
    markdown_file: str
    preview_image: str
    unit_path: Path
    
    @property
    def markdown_path(self) -> Path:
        return self.unit_path / self.markdown_file
    
    @property
    def preview_path(self) -> Path:
        return self.unit_path / self.preview_image

class UnitScanner:
    def __init__(self, base_path: str = "tutor-next/markdown"):
        self.base_path = Path(base_path)
        self.units: List[UnitMetadata] = []
        self._scan_units()
    
    def _scan_units(self) -> None:
        """Recursively scan for metadata.yml files and parse them"""
        for metadata_file in self.base_path.rglob("metadata.yml"):
            try:
                with open(metadata_file, 'r') as f:
                    metadata = yaml.safe_load(f)
                
                unit_path = metadata_file.parent
                self.units.append(UnitMetadata(
                    title=metadata['title'],
                    tags=metadata['tags'],
                    min_grade=metadata['minGrade'],
                    skill_level=metadata['skillLevel'],
                    subjects=metadata['subjects'],
                    skill_level_per_subject=metadata['skillLevelPerSubject'],
                    markdown_file=metadata['markdownFile'],
                    preview_image=metadata['previewImage'],
                    unit_path=unit_path
                ))
            except Exception as e:
                print(f"Error parsing {metadata_file}: {e}")
    
    def search(self, query: str, min_score: int = 60) -> List[UnitMetadata]:
        """
        Search units by title using fuzzy matching
        Args:
            query: Search string
            min_score: Minimum fuzzy match score (0-100)
        Returns:
            List of matching UnitMetadata objects
        """
        results = []
        for unit in self.units:
            score = fuzz.partial_ratio(query.lower(), unit.title.lower())
            if score >= min_score:
                results.append(unit)
        return sorted(results, key=lambda x: fuzz.partial_ratio(query.lower(), x.title.lower()), reverse=True)
    
    def list_all(self) -> List[UnitMetadata]:
        """Return all units"""
        return self.units
    
    def filter_by_subject(self, subject: str) -> List[UnitMetadata]:
        """Filter units by subject"""
        return [unit for unit in self.units if subject in unit.subjects]
    
    def filter_by_grade(self, grade: int) -> List[UnitMetadata]:
        """Filter units by minimum grade level"""
        return [unit for unit in self.units if unit.min_grade <= grade]
