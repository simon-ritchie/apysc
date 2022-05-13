"""This module is for running the test projects' E2E testing.

Command examples:
$ python scripts/run_test_projects_e2e_testing.py --alphabets_group abcdef
"""

import os
import sys
from argparse import ArgumentParser
from argparse import Namespace
from logging import Logger
from string import ascii_lowercase
from typing import List

from tqdm import tqdm
from typing_extensions import TypedDict

sys.path.append('./')

from apysc._console import loggers

logger: Logger = loggers.get_info_logger()


class _CommandOptions(TypedDict):
    alphabets_group: List[str]


def _main() -> None:
    """Entry point of this command.
    """
    command_options: _CommandOptions = _get_command_options()
    pass


def _get_command_options() -> _CommandOptions:
    """
    Get a command-line options.

    Returns
    -------
    options : _CommandOptions
        Command argument values and options.
    """
    from scripts import alphabets_group_param
    parser: ArgumentParser = ArgumentParser(
        description='The command for running the test projects\' '
        'E2E testing.')
    args: Namespace = parser.parse_args()
    alphabets_group: List[str] = alphabets_group_param.\
        split_alphabets_group_str(alphabets_group_str=args.alphabets_group)
    options: _CommandOptions = {
        'alphabets_group': alphabets_group,
    }
    return options


if __name__ == '__main__':
    _main()
