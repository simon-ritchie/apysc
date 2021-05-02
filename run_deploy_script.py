"""Deploying script (GitHub Actions) that handle linting, tests, and
PyPI uploading.

Command example:
$ python apply_lints.py
"""

import subprocess as sp
from logging import Logger

from apysc.console import loggers
from apply_lints import FLAKE8_COMMAND, NUMDOCLINT_COMMAND

logger: Logger = loggers.get_info_logger()


def _main() -> None:
    """Entry point of this command.
    """
    logger.info("Lint script started.")
    _run_flake8()


def _run_flake8() -> None:
    """
    Run flake8 command.

    Raises
    ------
    Exception
        If command standard out is not blank.
    """
    logger.info('flake8 command started.')
    stdout: str = _run_command(command=FLAKE8_COMMAND)
    if stdout != '':
        raise Exception('There are flake8 errors or warning.')


def _run_command(command: str) -> str:
    """
    Run lint command and return its stdout.

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


if __name__ == '__main__':
    _main()
