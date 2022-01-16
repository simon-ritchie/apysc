"""The flake8 command execution script. This is used by the deploying
job mainly.

Command example:
$ python ./scripts/run_flake8.py
"""

import sys
from logging import Logger

sys.path.append('./')

import scripts.command_util as command_util
from apysc._console import loggers
from scripts.apply_lints_and_build_docs import FLAKE8_COMMAND

logger: Logger = loggers.get_info_logger()


def _main() -> None:
    """
    Run the flake8 command.

    Raises
    ------
    Exception
        If command standard out is not blank.
    """
    logger.info('flake8 command started.')
    stdout: str = command_util.run_command(command=FLAKE8_COMMAND)
    if stdout != '':
        raise Exception('There are flake8 errors or warning.')


if __name__ == '__main__':
    _main()
