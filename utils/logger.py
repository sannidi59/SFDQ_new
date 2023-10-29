import logging
import os

_log_instance = None


def get_logger():
    global _log_instance
    if _log_instance is None:
        _log_instance = _setup_logger("ProjectLogger", "logs/project.log")
    return _log_instance


def _setup_logger(name, log_file, level=logging.INFO):
    """Setup logger"""
    if not os.path.exists('logs'):
        os.makedirs('logs')

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] - [%(filename)s:%(lineno)d] - %(message)s')

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

