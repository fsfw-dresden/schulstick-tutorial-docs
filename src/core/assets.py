import os
from typing import Optional
import pkg_resources
from pathlib import Path
from PyQt5.QtGui import QMovie, QPixmap

class AssetNotFoundError(Exception):
    """Raised when an asset file cannot be found"""
    pass

class Assets:
    """Helper class for managing static assets"""
    
    @staticmethod
    def get_asset_path(filename: str, module: Optional[str] = None) -> Path:
        """Get the full path to an asset file"""
        if module is None:
            module = 'static'
        try:
            # First try to get from installed package
            return Path(pkg_resources.resource_filename(module, f'assets/{filename}'))
        except (ImportError, pkg_resources.DistributionNotFound):
            # Fallback to local development path
            local_path = Path(__file__).parent.parent / module / 'assets' / filename
            if local_path.exists():
                return local_path
            raise AssetNotFoundError(f"Asset not found: {filename}")
    
    @staticmethod
    def load_movie(filename: str, module: Optional[str] = None) -> QMovie:
        """Load an animated asset file as QMovie"""
        movie = QMovie(str(Assets.get_asset_path(filename, module)))
        if not movie.isValid():
            raise AssetNotFoundError(f"Invalid movie asset: {filename}")
        return movie
    
    @staticmethod
    def load_pixmap(filename: str, module: Optional[str] = None) -> QPixmap:
        """Load an image asset file as QPixmap"""
        pixmap = QPixmap(str(Assets.get_asset_path(filename, module)))
        if pixmap.isNull():
            raise AssetNotFoundError(f"Invalid image asset: {filename}")
        return pixmap
