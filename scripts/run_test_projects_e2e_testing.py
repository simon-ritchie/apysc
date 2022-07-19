"""This module is for running the test projects' E2E testing.

Command examples:
$ python scripts/run_test_projects_e2e_testing.py --alphabets_group abcdef
"""

import os
import sys
from argparse import ArgumentParser
from argparse import Namespace
from logging import Logger
from typing import List

from typing_extensions import TypedDict

sys.path.append("./")

from apysc._console import loggers

logger: Logger = loggers.get_info_logger()


class _CommandOptions(TypedDict):
    alphabets_group: List[str]


def _main() -> None:
    """Entry point of this command."""
    command_options: _CommandOptions = _get_command_options()
    main_module_paths: List[str] = _get_target_test_project_main_module_paths(
        alphabets_group=command_options["alphabets_group"]
    )
    index_file_paths: List[str] = []
    for main_module_path in main_module_paths:
        _run_test_project_command(main_module_path=main_module_path)
        index_file_path: str = _get_index_file_path(main_module_path=main_module_path)
        if not os.path.isfile(index_file_path):
            continue
        index_file_paths.append(index_file_path)
    _run_e2e_testing(index_file_paths=index_file_paths)


def _run_e2e_testing(*, index_file_paths: List[str]) -> None:
    """
    Run an E2E testing of specified index.html's file paths.

    Parameters
    ----------
    index_file_paths : List[str]
        Target index.html's file paths.
    """
    from apysc._testing.e2e_testing_helper import LocalFileData
    from apysc._testing.e2e_testing_helper import assert_local_files_not_raise_error

    local_file_data_list: List[LocalFileData] = []
    for index_file_path in index_file_paths:
        file_path: str = f"file://{os.path.abspath(index_file_path)}"
        local_file_data_list.append(
            {
                "file_path": file_path,
                "expected_assertion_failed_msgs": None,
            }
        )
    assert_local_files_not_raise_error(local_file_data_list=local_file_data_list)


def _get_index_file_path(*, main_module_path: str) -> str:
    """
    Get a index.html's file path.

    Parameters
    ----------
    main_module_path : str
        A target main.py module path.

    Returns
    -------
    index_file_path : str
        A target index.html's file path.'
    """
    dir_path: str = os.path.dirname(main_module_path)
    index_file_path: str = os.path.join(dir_path, "test_output/index.html")
    return index_file_path


def _run_test_project_command(*, main_module_path: str) -> None:
    """
    Run a specified main.py module's test project command.

    Parameters
    ----------
    main_module_path : str
        A target main.py module's path.
    """
    from scripts import command_util

    stdout: str = command_util.run_command(command=f"python {main_module_path}")
    if "Traceback" in stdout:
        raise Exception(
            "There is an error in a test project's command."
            f"\nTarget module path: {main_module_path}"
            f"\nStdout:\n\n{stdout}"
        )


def _get_target_test_project_main_module_paths(
    *, alphabets_group: List[str]
) -> List[str]:
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
    project_dir_names: List[str] = os.listdir("./test_projects/")
    for project_dir_name in project_dir_names:
        first_lower_char: str = project_dir_name[0].lower()
        if first_lower_char not in alphabets_group:
            continue
        project_dir_path: str = os.path.join("./test_projects/", f"{project_dir_name}/")
        if not os.path.isdir(project_dir_path):
            continue
        main_module_path: str = os.path.join(project_dir_path, "main.py")
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
        description="The command for running the test projects' " "E2E testing."
    )
    alphabets_group_param.add_alphabets_group_arg_to_parser(parser=parser)
    args: Namespace = parser.parse_args()
    alphabets_group: List[str] = alphabets_group_param.split_alphabets_group_str(
        alphabets_group_str=args.alphabets_group
    )
    options: _CommandOptions = {
        "alphabets_group": alphabets_group,
    }
    return options


if __name__ == "__main__":
    _main()
