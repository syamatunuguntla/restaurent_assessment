import subprocess
import sys
from pathlib import Path

TABLE_DIR = Path(__file__).parent / "tables"

for script in sorted(TABLE_DIR.glob("*.py")):
    print(f"Running {script.name}")
    result = subprocess.run([sys.executable, str(script)])
    if result.returncode != 0:
        raise SystemExit(f"Failed: {script.name}")

print("Restaurant database setup completed.")
