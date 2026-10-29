import sys
from pathlib import Path

# Let `import config` and `import models` resolve from the server folder
# when Vercel loads this file from the project root.
SERVER_DIR = Path(__file__).resolve().parent / "server"
sys.path.insert(0, str(SERVER_DIR))

from app import app  # noqa: E402
