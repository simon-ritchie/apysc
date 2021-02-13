"""Build this project for PyPI.

Command example:
$ python build.py
"""

import shutil
import subprocess as sp
from logging import Logger
from typing import List

from apyscript.logging import loggers

logger: Logger = loggers.get_info_logger()


def _run_command(command: str) -> None:
    """
    Run the specified command.
    Parameters
    ----------
    command : str
        The command string.
    Raises
    ------
    Exception
        If the command return code is not 0.
    """
    logger.info(f'Command started: {command}')
    popen = sp.Popen(
        command, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
    stdout_bytes: bytes = popen.communicate()[0]
    try:
        stdout: str = stdout_bytes.decode('utf-8')
    except Exception:
        stdout = stdout_bytes.decode('sjis')
    logger.info(stdout)
    if popen.returncode == 0:
        return
    raise Exception(f'Command failed: {popen.returncode}')


_REMOVING_DIR_PATHS: List[str] = [
    './build',
    './dist',
    './stubdoc.egg-info',
]


def _remove_build_dirs() -> None:
    """
    Remove directories related to build process.
    """
    for removing_dir_path in _REMOVING_DIR_PATHS:
        shutil.rmtree(removing_dir_path, ignore_errors=True)


def _main() -> None:
    """Script entry point.
    """
    _remove_build_dirs()

    command: str = 'python setup.py sdist'
    _run_command(command=command)

    command = 'python setup.py bdist_wheel'
    _run_command(command=command)

    logger.info('Build completed!')


if __name__ == "__main__":
    _main()
