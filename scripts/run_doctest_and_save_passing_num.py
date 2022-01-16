"""The doctest runner command execution script and save the
passing tests number.
This is used by the deploying job mainly.

Command example:
$ python ./scripts/run_doctest_and_save_passing_num.py
"""

import re
from logging import Logger
from typing import List
from typing import Match
from typing import Optional

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
    logger.info("doctest command started.")
    stdout: str = command_util.run_command(
        command=(
            'pytest ./apysc/ --doctest-modules --workers auto -v -s'
        ))
    if ' failed, ' in stdout or 'Traceback' in stdout:
        raise Exception('There are failed tests.')
    _save_passing_tests_num(stdout=stdout)


def _save_passing_tests_num(stdout: str) -> None:
    """
    Save a passing tests number to the `.env` file.

    Parameters
    ----------
    stdout : str
        Test command stdout.
    """
    passing_test_num: str = _get_passing_test_num_from_stdout(
        stdout=stdout)
    logger.info('Saving a doctest passing tests number to the .env file.')
    with open('.env', 'a') as f:
        f.write(f'PASSING_TESTS_NUM="{passing_test_num}"\n')


def _get_passing_test_num_from_stdout(stdout: str) -> str:
    """
    Get a passing tests number from the stdout.

    Parameters
    ----------
    stdout : str
        Test command stdout.

    Returns
    -------
    passing_test_num : str
        Retrieved passing tests number.
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
    return passing_test_num


if __name__ == '__main__':
    _main()
