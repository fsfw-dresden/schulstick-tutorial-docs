import os
from pathlib import Path
from typing import List, Optional
from dataclasses import dataclass
import yaml
from appdirs import site_config_dir

@dataclass
class PortalConfig:
    """Configuration for the Schulstick Portal"""
    unit_paths: List[str]  # Paths to unit directories (relative or absolute)

    @classmethod
    def load(cls) -> 'PortalConfig':
        """Load config from appropriate location based on environment"""
        config_path = cls._get_config_path()
        
        if not config_path.exists():
            return cls.get_default_config()
            
        with open(config_path) as f:
            config_data = yaml.safe_load(f)
            
        return cls(
            unit_paths=config_data.get('unit_paths', ['tutor-next/markdown'])
        )
    
    @staticmethod
    def _get_config_path() -> Path:
        """Get the appropriate config file path based on environment"""
        if os.getenv('DEVELOPMENT'):
            return Path('./dev_config/schulstick-portal-config.yml')
        else:
            config_dir = site_config_dir('schulstick', multipath=True)
            return Path(config_dir) / 'schulstick-portal-config.yml'
    
    @classmethod
    def get_default_config(cls) -> 'PortalConfig':
        """Return default configuration"""
        return cls(
            unit_paths=['tutor-next/markdown']
        )
