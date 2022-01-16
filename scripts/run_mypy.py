"""The mypy command execution script. This is used by the deploying
job mainly.

Command example:
$ python ./scripts/run_mypy.py
"""

from logging import Logger

import command_util
from scripts.apply_lints_and_build_docs import MYPY_COMMAND
from apysc._console import loggers

logger: Logger = loggers.get_info_logger()


def _main() -> None:
    """
    Run the mypy command.

    Raises
    ------
    Exception
        If there are any mypy errors.
    """
    logger.info('mypy command started.')
    stdout: str = command_util.run_command(command=MYPY_COMMAND)
    if 'Success' not in stdout:
        raise Exception('There are mypy errors.')


if __name__ == '__main__':
    _main()
