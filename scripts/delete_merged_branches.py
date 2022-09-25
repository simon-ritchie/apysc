"""Run the script to delete merged Git branches.

Command example:
$ python ./scripts/delete_merged_branches.py
"""

import sys
from logging import Logger
from typing import List

sys.path.append("./")

import scripts.command_util as command_util
from apysc._console import loggers

logger: Logger = loggers.get_info_logger()


def _main() -> None:
    """
    Run the script to delete merged Git branches.
    """
    merged_branch_names: List[str] = _get_merged_branch_names()
    pass


def _get_merged_branch_names() -> List[str]:
    """
    Get merged Git branch names.

    Returns
    -------
    merged_branch_names : List[str]
        Merged Git branch names.
    """
    stdout: str = command_util.run_command(command="git branch --merged")
    lines: List[str] = stdout.splitlines()
    merged_branch_names: List[str] = []
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        if not line.startswith("#"):
            continue
        merged_branch_names.append(line)
    return merged_branch_names


if __name__ == "__main__":
    _main()
