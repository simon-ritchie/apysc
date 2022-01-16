"""The numdoclint command execution script. This is used by the
deploying job mainly.

Command example:
$ python ./scripts/run_numdoclint.py
"""

from logging import Logger
import sys

sys.path.append('./')

import scripts.command_util as command_util
from scripts.apply_lints_and_build_docs import NUMDOCLINT_COMMAND
from apysc._console import loggers

logger: Logger = loggers.get_info_logger()


def _main() -> None:
    """
    Run the numdoclint command.

    Raises
    ------
    Exception
        If command standard out is not blank.
    """
    logger.info('numdoclint command started.')
    stdout: str = command_util.run_command(command=NUMDOCLINT_COMMAND)
    if stdout != '':
        raise Exception('There are numdoclint errors.')


if __name__ == '__main__':
    _main()
