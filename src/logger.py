import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
LOG_path = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.info("Logging has started.")
