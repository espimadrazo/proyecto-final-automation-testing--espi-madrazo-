import logging
import os

#CREATION AND BASIC LOG CONFIGURATION FOR TEST EXECUTION DETAILS
os.makedirs("logs", exist_ok = True) #Create log directory

logging.basicConfig(
    filename="logs/execution.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    force=True
    )

logger = logging.getLogger(__name__)