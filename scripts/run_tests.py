"""The test runner command execution script. This is used by the
deploying job mainly.

Command example:
$ python ./scripts/run_tests.py
"""

from logging import Logger
import sys

sys.path.append('./')

import scripts.command_util as command_util
from apysc._console import loggers

logger: Logger = loggers.get_info_logger()


def _main() -> None:
    """
    Run the testing command.

    Raises
    ------
    Exception
        If there are any failed tests.
    """
    logger.info('testing command started.')
    stdout: str = command_util.run_command(
        command=(
            'pytest tests/ -v -s --workers auto'
        ))
    if ' failed, ' in stdout or 'Traceback' in stdout:
        raise Exception('There are failed tests.')


if __name__ == '__main__':
    _main()
