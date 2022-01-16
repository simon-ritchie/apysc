"""The numdoclint command execution script. This is used by the
deploying job mainly.

Command example:
$ python ./scripts/run_numdoclint.py
"""

import sys
from logging import Logger

sys.path.append('./')

import scripts.command_util as command_util
from apysc._console import loggers
from scripts.apply_lints_and_build_docs import NUMDOCLINT_COMMAND

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
