"""The test runner command execution script. This is used by the
deploying job mainly.

Command example:
$ python run_tests.py
"""

import re
from logging import Logger
from typing import List, Match, Optional

import command_util
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
