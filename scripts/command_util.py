"""Common command utility implementations.
"""

import subprocess as sp
import sys
from logging import Logger

sys.path.append('./')

from apysc._console import loggers

logger: Logger = loggers.get_info_logger()


def run_command(command: str) -> str:
    """
    Run the specified command and return its stdout.

    Parameters
    ----------
    command : str
        Target lint command.

    Returns
    -------
    stdout : str
        Command result stdout.
    """
    logger.info(f'Target command: {command}')
    complete_process: sp.CompletedProcess = sp.run(
        command, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
    stdout: str = complete_process.stdout.decode('utf-8')
    stdout = stdout.strip()
    if stdout == '[]':
        stdout = ''
    print(stdout)
    return stdout
