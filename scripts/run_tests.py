"""The test runner command execution script. This is used by the
deploying job mainly.

Command example:
$ python ./scripts/run_tests.py
"""

import sys
from logging import Logger

sys.path.append("./")

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
    import scripts.command_util as command_util
    from apysc._string import string_util

    logger.info("testing command started.")
    stdout: str = command_util.run_command(command=("pytest tests/ -v -s"))
    tail_stdout: str = string_util.get_tails_lines_str(string=stdout, n=10)
    if " failed, " in tail_stdout:
        raise Exception("There are failed tests.")


if __name__ == "__main__":
    _main()
