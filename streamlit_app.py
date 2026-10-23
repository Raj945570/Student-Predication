import sys
from pathlib import Path
import runpy

# Ensure root directory and app directory are accessible in python path
ROOT_DIR = Path(__file__).resolve().parent
APP_DIR = ROOT_DIR / "Streamlit_App"

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

# Delegate to the main Streamlit application
runpy.run_path(str(APP_DIR / "app.py"), run_name="__main__")
