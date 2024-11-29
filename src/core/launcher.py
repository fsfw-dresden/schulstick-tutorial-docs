import logging
import subprocess
from pathlib import Path
from typing import Optional
from .models import UnitMetadata

logger = logging.getLogger(__name__)

class ProgramLauncher:
    """Helper class for launching external programs"""
    
    @staticmethod
    def launch_program(unit: UnitMetadata) -> Optional[subprocess.Popen]:
        """
        Launch a program specified in the unit's program_launch_info
        
        Args:
            unit: UnitMetadata containing program launch information
            
        Returns:
            subprocess.Popen object if launch successful, None otherwise
        """
        if not unit.program_launch_info:
            return None
            
        try:
            cmd = [unit.program_launch_info.bin_name]
            
            # Add optional path if specified
            if unit.program_launch_info.path:
                path = Path(unit.program_launch_info.path)
                if path.exists():
                    cmd.append(str(path))
                    
            # Add optional arguments
            if unit.program_launch_info.args:
                cmd.extend(unit.program_launch_info.args)
                
            logger.info(f"Launching program: {' '.join(cmd)}")
            
            # Launch program
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            return process
            
        except (subprocess.SubprocessError, FileNotFoundError) as e:
            logger.error(f"Failed to launch program: {e}")
            return None
