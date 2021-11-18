"""Deploying script (GitHub Actions) that handle linting, tests, and
PyPI uploading.

Command example:
$ python apply_lints.py
"""

import re
from logging import Logger
from typing import List
from typing import Match
from typing import Optional

import command_util
from apysc import __version__
from apysc._console import loggers

logger: Logger = loggers.get_info_logger()


def _main() -> None:
    """Entry point of this command.
    """
    logger.info('Lint script started.')
    _run_tests()
    _build()
    _save_version_env_var()


def _save_version_env_var() -> None:
    """
    Save version number to .env file.
    """
    logger.info('Saving version number file.')
    with open('.env', 'a') as f:
        f.write(f'VERSION="{__version__}"\n')


def _build() -> None:
    """
    Run build command.

    Raises
    ------
    Exception
        If there is any Traceback.
    """
    logger.info('Build command started.')
    stdout: str = command_util.run_command(command='python build.py')
    if 'Traceback' in stdout:
        raise Exception('There is build command error.')


def _run_tests() -> None:
    """
    Run testing command.

    Raises
    ------
    Exception
        If there are any failed tests.
    """
    logger.info('testing command started.')
    stdout: str = command_util.run_command(
        command=(
            'pytest --cov=./apysc tests/ -v -s --workers auto '
            '--cov-report term-missing'
        ))
    if ' failed, ' in stdout:
        raise Exception('There are failed tests.')
    _save_coverage(stdout=stdout)


def _save_coverage(stdout: str) -> None:
    """
    Svae test coverage to .env file.

    Parameters
    ----------
    stdout : str
        Test command stdout.
    """
    lines: List[str] = stdout.splitlines()
    coverage: str = ''
    for line in lines:
        if not line.startswith('TOTAL '):
            continue
        match: Optional[Match] = re.search(
            pattern=r'(\d+?\%)', string=line)
        if match is None:
            raise Exception('Test coverage value is missing.')
        coverage = match.group(1)
    logger.info('Saving version number file.')
    with open('.env', 'a') as f:
        f.write(f'COVERAGE="{coverage}"\n')


if __name__ == '__main__':
    _main()
