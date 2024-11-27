import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from core.models import UnitMetadata
from tutor.tutor import TutorView

def main():
    # Enable high DPI scaling
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    app = QApplication(sys.argv)
    
    if len(sys.argv) > 1:
        # Load unit from provided directory
        unit_dir = Path(sys.argv[1])
        if not unit_dir.exists():
            print(f"Error: Directory {unit_dir} does not exist")
            sys.exit(1)
            
        metadata_file = unit_dir / "metadata.yml"
        if not metadata_file.exists():
            print(f"Error: No metadata.yml found in {unit_dir}")
            sys.exit(1)
            
        try:
            unit = UnitMetadata.from_yaml_file(metadata_file)
            unit.unit_path = unit_dir
            tutor = TutorView(unit)
            tutor.show()
            return app.exec_()
        except Exception as e:
            print(f"Error loading unit: {e}")
            sys.exit(1)
    else:
        print("Usage: python -m tutor.main <unit_directory>")
        sys.exit(1)

if __name__ == "__main__":
    sys.exit(main())
