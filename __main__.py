# __main__.py
import sys
from pathlib import Path

# Add the py/ folder to sys.path so we can import main.py
repo_root = Path(__file__).parent
py_folder = repo_root / "py"
sys.path.insert(0, str(py_folder))

import main  # this runs py/main.py