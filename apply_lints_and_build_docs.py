"""Apply each lint to all modules and build documentation.

Command example:
$ python apply_lints_and_build_docs.py
$ python apply_lints_and_build_docs.py --skip_overall_docs_build
"""

import multiprocessing as mp
import os
import re
import shutil
import subprocess as sp
from argparse import ArgumentParser
from argparse import Namespace
from logging import Logger
from typing import List
from typing import Match
from typing import Optional
from typing import Tuple

from typing_extensions import Final
from typing_extensions import TypedDict

from apysc._console import loggers
from apysc._file import module_util
from apysc._lint import lint_hash_util

logger: Logger = loggers.get_info_logger()


class LintCommand(TypedDict):
    command: str
    lint_name: str


FLAKE8_NO_PATH_COMMAND: Final[str] = (
    'flake8 --ignore E402,W503'
)

FLAKE8_COMMAND: Final[str] = (
    f'{FLAKE8_NO_PATH_COMMAND} ./'
)

NUMDOCLINT_COMMAND: Final[str] = (
    'numdoclint -p ./ -r -f test,sample,_test,_sample,mock_'
)

MYPY_NO_PATH_COMMAND: Final[str] = (
    'mypy --ignore-missing-imports --follow-imports skip '
    '--disallow-untyped-calls --disallow-untyped-defs '
    '--strict-optional --strict-equality'
)

MYPY_COMMAND: Final[str] = (
    f'{MYPY_NO_PATH_COMMAND} ./apysc/ '
    './tests/ ./test_projects/'
)


def _get_module_paths() -> List[str]:
    """
    Get the Python module paths in the project.

    Returns
    -------
    module_paths : list of str
        Python module paths in the project.
    """
    logger.info('Getting module paths...')
    dir_paths: List[str] = [
        './apysc/',
        './docs_src/',
        './tests/',
        './test_projects/',
    ]
    with mp.Pool(processes=len(dir_paths)) as p:
        module_paths_list: List[List[str]] = p.map(
            func=module_util.get_module_paths_recursively,
            iterable=dir_paths)
    module_paths: List[str] = []
    for module_paths_ in module_paths_list:
        module_paths.extend(module_paths_)

    root_module_paths: List[str] = _get_root_dir_module_paths()
    module_paths.extend(root_module_paths)
    return module_paths


def _get_root_dir_module_paths() -> List[str]:
    """
    Get root directory module paths.

    Returns
    -------
    module_paths : list of str
        Root directory module paths.
    """
    filr_or_dir_names: List[str] = os.listdir('./')
    module_paths: List[str] = []
    for file_or_dir_name in filr_or_dir_names:
        if not os.path.isfile(file_or_dir_name):
            continue
        if not file_or_dir_name.endswith('.py'):
            continue
        if file_or_dir_name.startswith('__init__'):
            continue
        if 'tmp' in file_or_dir_name:
            continue
        module_paths.append(f'./{file_or_dir_name}')
    return module_paths


class _CommandOptions(TypedDict):
    skip_overall_docs_build: bool


def _main() -> None:
    """Entry point of this command.
    """
    from build_docs import HASHED_VALS_DIR_PATH
    options: _CommandOptions = _get_command_options()
    shutil.rmtree('./build/', ignore_errors=True)
    if not options['skip_overall_docs_build']:
        shutil.rmtree(HASHED_VALS_DIR_PATH, ignore_errors=True)
    _remove_tmp_py_module()

    logger.info(msg='Documentation build started.')
    process: sp.Popen = sp.Popen(
        ['python', 'build_docs.py'], stdout=sp.PIPE, stderr=sp.PIPE)

    lint_commands: List[LintCommand]
    updated_module_paths: List[str]
    lint_commands, updated_module_paths, = _make_lint_commands()
    for lint_command in lint_commands:
        run_lint_command(lint_command=lint_command)

    hash_lint_types: List[lint_hash_util.LintType] = [
        lint_hash_util.LintType.AUTOFLAKE,
        lint_hash_util.LintType.ISORT,
        lint_hash_util.LintType.AUTOPEP8,
    ]
    for hash_lint_type in hash_lint_types:
        logger.info(
            msg=f'Saving {hash_lint_type.value} hash files...')
        lint_hash_util.save_target_modules_hash(
            module_paths=updated_module_paths,
            lint_type=hash_lint_type)

    stdout: bytes
    stderr: bytes
    logger.info(msg='Waiting documentation build completion...')
    stdout, stderr = process.communicate()
    stdout_str: str = stdout.decode()
    stderr_str: str = stderr.decode()
    for string in (stdout_str, stderr_str):
        if 'Traceback' not in string:
            continue
        print(string)
    logger.info(msg='Ended.')


_MkCommandReturns = Tuple[
    List[LintCommand], List[str]]


def _make_lint_commands() -> _MkCommandReturns:
    """
    Make the lint commands list.

    Returns
    -------
    lint_commands : list of LintCommand
        Created lint commands data list.
    updated_module_paths : list of str
        Updated target module paths.
    """
    module_paths: List[str] = _get_module_paths()

    lint_commands: List[LintCommand] = []

    autoflake_updated_module_paths: List[str] = \
        _append_autoflake_lint_command_if_module_updated(
            lint_commands=lint_commands, module_paths=module_paths)

    isort_updated_module_paths: List[str] = \
        _append_isort_lint_command_if_module_updated(
            lint_commands=lint_commands, module_paths=module_paths)

    autopep8_updated_module_paths: List[str] = \
        _append_autopep8_lint_command_if_module_updated(
            lint_commands=lint_commands, module_paths=module_paths)

    lint_commands.extend([{
        'command': FLAKE8_COMMAND,
        'lint_name': 'flake8',
    }, {
        'command': NUMDOCLINT_COMMAND,
        'lint_name': 'numdoclint',
    }, {
        'command': MYPY_COMMAND,
        'lint_name': 'mypy',
    }])

    updated_module_paths: List[str] = [
        *autoflake_updated_module_paths,
        *isort_updated_module_paths,
        *autopep8_updated_module_paths]
    updated_module_paths = list(set(updated_module_paths))

    return lint_commands, updated_module_paths


def _append_isort_lint_command_if_module_updated(
        lint_commands: List[LintCommand],
        module_paths: List[str]) -> List[str]:
    """
    Append the isort lint command to the list if the
    modules have been updated.

    Parameters
    ----------
    lint_commands : list of LintCommand
        Target list.
    module_paths : list of str
        Overall module paths.

    Returns
    -------
    isort_updated_module_paths : list of str
        Updated module paths.
    """
    logger.info(msg='Creating the isort command...')
    isort_updated_module_paths: List[str] = lint_hash_util.\
        remove_not_updated_module_paths(
            module_paths=module_paths,
            lint_type=lint_hash_util.LintType.ISORT)
    if isort_updated_module_paths:
        isort_module_paths_str: str = _get_joined_paths_str(
            module_paths=isort_updated_module_paths)
        lint_commands.append({
            'command': 'isort --force-single-line-imports '
            f'{isort_module_paths_str}',
            'lint_name': 'isort',
        })
    return isort_updated_module_paths


def _append_autopep8_lint_command_if_module_updated(
        lint_commands: List[LintCommand],
        module_paths: List[str]) -> List[str]:
    """
    Append the autopep8 lint command to the list if the
    modules have been updated.

    Parameters
    ----------
    lint_commands : list of LintCommand
        Target list.
    module_paths : list of str
        Overall module paths.

    Returns
    -------
    autopep8_updated_module_paths : list of str
        Updated module paths.
    """
    logger.info(msg='Creating the autopep8 command...')
    autopep8_updated_module_paths: List[str] = lint_hash_util.\
        remove_not_updated_module_paths(
            module_paths=module_paths,
            lint_type=lint_hash_util.LintType.AUTOPEP8)
    if autopep8_updated_module_paths:
        autopep8_module_paths_str: str = _get_joined_paths_str(
            module_paths=autopep8_updated_module_paths)
        lint_commands.append({
            'command':
            'autopep8 --in-place --aggressive --aggressive --ignore=E402 '
            f'{autopep8_module_paths_str}',
            'lint_name': 'autopep8',
        })
    return autopep8_updated_module_paths


def _append_autoflake_lint_command_if_module_updated(
        lint_commands: List[LintCommand],
        module_paths: List[str]) -> List[str]:
    """
    Append the autoflake lint command to the list if the
    modules have been updated.

    Parameters
    ----------
    lint_commands : list of LintCommand
        Target list.
    module_paths : list of str
        Overall module paths.

    Returns
    -------
    autoflake_updated_module_paths : list of str
        Updated module paths.
    """
    logger.info(msg='Creating the autoflake command...')
    autoflake_updated_module_paths: List[str] = lint_hash_util.\
        remove_not_updated_module_paths(
            module_paths=module_paths,
            lint_type=lint_hash_util.LintType.AUTOFLAKE)
    if autoflake_updated_module_paths:
        autoflake_module_paths_str: str = _get_joined_paths_str(
            module_paths=autoflake_updated_module_paths)
        lint_commands.append({
            'command':
            'autoflake --in-place --remove-unused-variables '
            '--remove-all-unused-imports '
            f'{autoflake_module_paths_str}',
            'lint_name': 'autoflake',
        })
    return autoflake_updated_module_paths


def _get_joined_paths_str(module_paths: List[str]) -> str:
    """
    Get a joined paths string for a lint command.

    Parameters
    ----------
    module_paths : list of str
        Target module paths.

    Returns
    -------
    joined_paths_str : str
        A joined paths string for a lint command.
    """
    joined_paths_str: str = ' '.join(module_paths)
    return joined_paths_str


def _get_command_options() -> _CommandOptions:
    """
    Get a command-line options.

    Returns
    -------
    options : _CommandOptions
        Command argument values and options.
    """
    parser: ArgumentParser = ArgumentParser(
        description='Apply each lint to all modules and build documentation.')

    parser.add_argument(
        '-s',
        '--skip_overall_docs_build',
        action='store_true',
        help='If specified, build the overall documentation. If not '
        'specified, only updated document will be built.',
    )
    args: Namespace = parser.parse_args()
    options: _CommandOptions = {
        'skip_overall_docs_build': args.skip_overall_docs_build,
    }
    return options


def _remove_tmp_py_module() -> None:
    """
    Remove temporary Python modules (`tmp_<any_string>.py` file
    will become deletion target).
    """
    file_names: List[str] = os.listdir('./')
    for file_name in file_names:
        if not os.path.isfile(file_name):
            continue
        match: Optional[Match] = re.search(
            pattern=r'tmp_.+\.py$',
            string=file_name)
        if match is None:
            continue
        os.remove(file_name)


def run_command(command: str) -> str:
    """
    Run a specified command.

    Parameters
    ----------
    command : str
        Target command string.

    Returns
    -------
    stdout : str
        Command result stdout.
    """
    complete_process: sp.CompletedProcess = sp.run(
        command, shell=True,
        stdout=sp.PIPE, stderr=sp.STDOUT)
    stdout: str = complete_process.stdout.decode('utf-8')
    return stdout


def run_lint_command(lint_command: LintCommand) -> str:
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
    stdout: str = run_command(command=lint_command['command'])
    print(stdout)
    return stdout


if __name__ == '__main__':
    _main()
