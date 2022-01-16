"""The mypy command execution script. This is used by the deploying
job mainly.

Command example:
$ python ./scripts/run_mypy.py
"""

import sys
from logging import Logger

sys.path.append('./')

import scripts.command_util as command_util
from apysc._console import loggers
from scripts.apply_lints_and_build_docs import MYPY_COMMAND

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
