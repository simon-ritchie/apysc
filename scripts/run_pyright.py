"""The Pyright command execution script. This is used by the
deploying job mainly.

Command example:
$ python ./scripts/run_pyright.py
"""

import sys
from logging import Logger
from typing import List

sys.path.append('./')

import scripts.command_util as command_util
from apysc._console import loggers
from scripts.apply_lints_and_build_docs import PYRIGHT_COMMAND

logger: Logger = loggers.get_info_logger()


def _main() -> None:
    """
    Run the Pyright command.

    Raises
    ------
    Exception
        If there are any Pyright errors.
    """
    logger.info('Pyright command started.')
    stdout: str = command_util.run_command(command=PYRIGHT_COMMAND)
    lines: List[str] = stdout.splitlines()
    for line in lines:
        if line.startswith('0 errors'):
            return
    raise Exception('There are Pyright errors.')


if __name__ == '__main__':
    _main()
