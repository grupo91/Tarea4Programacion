
# logger_config.py
# configures the loogging system to store errors in a file.


import logging

logging.basicConfig(
    filename="system.log",  # log filename
    level=logging.ERROR,    # only errors will be logged
    format="%(asctime)s - %(levelname)s - %(message)s"
)

