
# logger_config.py
# configures the loing system to store erors in a file.


import logging

logging.basicConfig(
    filename="system.log",  # log file name
    level=logging.ERROR,    # only erors will be logged
    format="%(asctime)s - %(levelname)s - %(message)s"
)

