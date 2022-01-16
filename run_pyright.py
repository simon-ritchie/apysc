"""The Pyright command execution script. This is used by the
deploying job mainly.

Command example:
$ python run_pyright.py
"""

from logging import Logger
from typing import List

import command_util
from scripts.apply_lints_and_build_docs import PYRIGHT_COMMAND
from apysc._console import loggers

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
