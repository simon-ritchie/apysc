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
    main_module_paths: List[str] = _get_target_test_project_main_module_paths(
        alphabets_group=command_options['alphabets_group'])
    pass


def _get_target_test_project_main_module_paths(
        *, alphabets_group: List[str]) -> List[str]:
    """
    Get target test projects' main.py module paths.

    Parameters
    ----------
    alphabets_group : List[str]
        A target alphabets group characters' list.

    Returns
    -------
    main_module_paths : List[str]
        Target test projects' main.py module paths.
    """
    main_module_paths: List[str] = []
    project_dir_names: List[str] = os.listdir('./test_projects/')
    for project_dir_name in project_dir_names:
        first_lower_char: str = project_dir_name[0].lower()
        if first_lower_char not in alphabets_group:
            continue
        project_dir_path: str = os.path.join(
            './test_projects/', f'{project_dir_name}/')
        if not os.path.isdir(project_dir_path):
            continue
        main_module_path: str = os.path.join(project_dir_path, 'main.py')
        if not os.path.exists(main_module_path):
            continue
        main_module_paths.append(main_module_path)
    return main_module_paths


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
