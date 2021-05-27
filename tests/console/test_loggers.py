from logging import INFO

from apysc.console import loggers


def test_get_info_logger() -> None:
    logger = loggers.get_info_logger()
    assert logger.level == INFO
    assert logger.name == loggers._LOGGER_NAME_INFO

    logger = loggers.get_info_logger()
    assert len(logger.handlers) == 1
