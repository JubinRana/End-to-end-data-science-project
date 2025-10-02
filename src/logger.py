import logging
import os
from datetime import datetime
import sys

# ------------------------------
# Step 1: Determine project root
# ------------------------------
try:
    # Project root assumed as one level above src/
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    LOGS_DIR = os.path.join(PROJECT_ROOT, "logs")
    os.makedirs(LOGS_DIR, exist_ok=True)
    print(f"[INFO] Logs folder ensured at: {LOGS_DIR}")
except Exception as e:
    print(f"[ERROR] Could not create logs folder: {e}")
    sys.exit(1)

# ------------------------------
# Step 2: Create log file path
# ------------------------------
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)
print(f"[INFO] Log file will be created at: {LOG_FILE_PATH}")

# ------------------------------
# Step 3: Configure logging
# ------------------------------
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] %(levelname)s - %(message)s",
)

# Optional: Also log to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter("[ %(asctime)s ] %(levelname)s - %(message)s")
console_handler.setFormatter(console_formatter)
logging.getLogger().addHandler(console_handler)

# ------------------------------
# Step 4: Test logging
# ------------------------------
if __name__ == "__main__":
    try:
        logging.info("Logging system started successfully!")
        logging.info("This is a test log message.")
        print("[INFO] Script finished. Check the logs folder in the project root.")
    except Exception as e:
        print(f"[ERROR] Logging failed: {e}")

