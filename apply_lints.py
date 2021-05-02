"""Apply each lints to all modules.

Command example:
$ python apply_lints.py
"""

import shutil
import subprocess as sp
from logging import Logger
from typing import List

from typing_extensions import TypedDict, Final

from apysc.console import loggers

logger: Logger = loggers.get_info_logger()


class LintCommand(TypedDict):
    command: str
    lint_name: str


FLAKE8_COMMAND: Final[str] = (
    'flake8 --ignore E402,W503 ./'
)

NUMDOCLINT_COMMAND: Final[str] = (
    'numdoclint -p ./ -r -f test,sample,_test,_sample'
)


lint_commands: List[LintCommand] = [
    {
        'command':
        'autoflake --in-place --remove-unused-variables '
        '--remove-all-unused-imports -r .',
        'lint_name': 'autoflake',
    }, {
        'command': 'isort --force-single-line-imports .',
        'lint_name': 'isort',
    }, {
        'command':
        'autopep8 --in-place --aggressive --aggressive -r --ignore=E402 .',
        'lint_name': 'autopep8',
    }, {
        'command': FLAKE8_COMMAND,
        'lint_name': 'flake8',
    }, {
        'command': NUMDOCLINT_COMMAND,
        'lint_name': 'numdoclint',
    }, {
        'command':
        'mypy --ignore-missing-imports --follow-imports skip '
        '--disallow-untyped-calls --disallow-untyped-defs '
        '--strict-optional --strict-equality ./apysc/ '
        './tests/ ./test_projects/',
        'lint_name': 'mypy',
    },
]


def _main() -> None:
    """Entry point of this command.
    """
    shutil.rmtree('./build/', ignore_errors=True)
    for lint_command in lint_commands:
        _run_lint_command(lint_command=lint_command)


def _run_lint_command(lint_command: LintCommand) -> str:
    """
    Run single lint command.

    Parameters
    ----------
    lint_command : str
        Target lint command settng.

    Returns
    -------
    stdout : str
        Command result stdout.
    """
    print('-' * 20)
    logger.info(msg=f'{lint_command["lint_name"]} command started.')
    complete_process: sp.CompletedProcess = sp.run(
        lint_command['command'], shell=True,
        stdout=sp.PIPE, stderr=sp.STDOUT)
    stdout: str = complete_process.stdout.decode('utf-8')
    print(stdout)
    return stdout


if __name__ == '__main__':
    _main()
