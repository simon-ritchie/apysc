"""The test runner command execution script and save the
test coverage and passing tests number.
This is used by the deploying job mainly.

Command example:
$ python ./scripts/run_tests_and_save_coverage_and_num.py
"""

import re
from logging import Logger
from typing import List
from typing import Match
from typing import Optional
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
            'pytest --cov=./apysc tests/ -v -s --workers auto '
            '--cov-report term-missing'
        ))
    if ' failed, ' in stdout or 'Traceback' in stdout:
        raise Exception('There are failed tests.')
    _save_coverage(stdout=stdout)
    _save_passing_tests_num(stdout=stdout)


def _save_passing_tests_num(stdout: str) -> None:
    """
    Save a passing tests number to the `.env` file.

    Parameters
    ----------
    stdout : str
        Test command stdout.
    """
    lines: List[str] = stdout.splitlines()
    passing_test_num: str = ''
    for line in lines:
        if ' passed in ' not in line:
            continue
        match: Optional[Match] = re.search(
            pattern=r'.*? (\d+?) passed',
            string=line)
        if match is None:
            continue
        passing_test_num = match.group(1)
    logger.info('Saving a passing tests number to the .env file.')
    with open('.env', 'a') as f:
        f.write(f'PASSING_TESTS_NUM="{passing_test_num}"\n')


def _save_coverage(stdout: str) -> None:
    """
    Save a test coverage to the `.env` file.

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
            pattern=r'TOTAL\s+?(\d+?)\s+?(\d+?)\s',
            string=line)
        if match is None:
            raise Exception('Test coverage value is missing.')
        statements: int = int(match.group(1))
        missed: int = int(match.group(2))
        coverage_float: float = 100 - (missed / statements) * 100
        coverage = f'{coverage_float:.2f}%'
    logger.info('Saving a coverage to the .env file.')
    with open('.env', 'a') as f:
        f.write(f'COVERAGE="{coverage}"\n')


if __name__ == '__main__':
    _main()
