import os
import sys
import logging

# Define the logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory and filepath for log files
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging settings
logging.basicConfig(
    level= logging.INFO,  # Set logging level to INFO
    format= logging_str,  # Use the defined logging format

    # Define logging handlers (writing to a file and printing to stdout)
    handlers=[
        logging.FileHandler(log_filepath),  # Log to a file
        logging.StreamHandler(sys.stdout)   # Print to console
    ]
)

# Get or create a logger named "cnnClassifierLogger"
logger = logging.getLogger("cnnClassifierLogger")