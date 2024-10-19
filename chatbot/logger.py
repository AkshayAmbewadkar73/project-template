import logging
import os
from datetime import datetime

# Create log file name with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log path and ensure the directory exists
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

# Full path to the log file
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure logging to write both to a file and console
logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILEPATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

# Test the logger
if __name__ == "__main__":
    logging.info("Here again, I am testing.")