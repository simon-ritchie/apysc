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
    for merged_branch_name in merged_branch_names:
        logger.info(f"Deleting the {merged_branch_name} branch...")
        stdout: str = command_util.run_command(
            command=f"git push --delete origin \\{merged_branch_name} -f"
        )
        print(stdout)
        break


def _get_merged_branch_names() -> List[str]:
    """
    Get merged Git branch names.

    Returns
    -------
    merged_branch_names : List[str]
        Merged Git branch names.
    """
    stdout: str = command_util.run_command(command="git branch -a --merged")
    lines: List[str] = stdout.splitlines()
    merged_branch_names: List[str] = []
    for line in lines:
        line = line.strip()
        if not line.startswith("#"):
            continue
        merged_branch_names.append(line)
    return merged_branch_names


if __name__ == "__main__":
    _main()
