# logger_config.py
# Configures logging system for the application.

import logging
import os


def setup_logger(log_file: str = "system.log") -> logging.Logger:
    """
    Configure and return a logger for the system.
    
    This logger will:
    - Save logs to a file
    - Display logs in console
    - Format logs with timestamps and levels
    
    Args:
        log_file (str): Name of the log file
    
    Returns:
        logging.Logger: Configured logger instance
    """

    # Crear carpeta logs si no existe
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_path = os.path.join(log_dir, log_file)

    # Crear logger
    logger = logging.getLogger("SoftwareFJ")
    logger.setLevel(logging.DEBUG)  # Captura todo

    # Evitar duplicación de logs
    if logger.hasHandlers():
        return logger

    # Formato de logs
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Handler para archivo
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Handler para consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Agregar handlers al logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Función auxiliar para registrar excepciones
def log_exception(logger: logging.Logger, error: Exception):
    """
    Log an exception with full details.
    
    Args:
        logger (Logger): Logger instance
        error (Exception): Exception to log
    """
    logger.error(f"Exception occurred: {str(error)}", exc_info=True)