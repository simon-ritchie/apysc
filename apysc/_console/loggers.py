"""Definitions and interface for loggers.
"""

from logging import INFO
from logging import Formatter
from logging import Logger
from logging import StreamHandler
from logging import getLogger

_LOGGER_NAME_INFO: str = "user_info"
_is_initial_call: bool = True


def get_info_logger() -> Logger:
    """
    Get information logger.

    Returns
    -------
    logger : Logger
        Information logger as following settings.
        - Level: INFO
        - Format: `%Y-%m-%d %H:%M:%S. <message>`
    """
    global _is_initial_call
    logger: Logger = getLogger(_LOGGER_NAME_INFO)
    logger.setLevel(level=INFO)

    if _is_initial_call:
        stream_handler: StreamHandler = StreamHandler()
        formatter: Formatter = Formatter(
            fmt="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        stream_handler.setFormatter(fmt=formatter)
        logger.addHandler(stream_handler)
        _is_initial_call = False
    return logger
