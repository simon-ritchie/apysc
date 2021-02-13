from logging import INFO

from apyscript.logging import loggers


def test_get_info_logger() -> None:
    logger = loggers.get_info_logger()
    assert logger.level == INFO
    assert logger.name == loggers._LOGGER_NAME_INFO
