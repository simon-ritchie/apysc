"""Lint script for deploying (GitHub Actions).

Command example:
$ python apply_lints.py
"""

from logging import Logger

from apysc.console import loggers

logger: Logger = loggers.get_info_logger()


def _main() -> None:
    """Entry point of this command.
    """
    logger.info("Lint script started.")


if __name__ == '__main__':
    _main()
