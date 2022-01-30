"""Apply each lint to all modules and build documentation.

Command example:
$ python scripts/apply_lints_and_build_docs.py
$ python scripts/apply_lints_and_build_docs.py --skip_overall_docs_build
"""

import multiprocessing as mp
import os
import re
import shutil
import subprocess as sp
import sys
from argparse import ArgumentParser
from argparse import Namespace
from datetime import datetime
from logging import Logger
from typing import List
from typing import Match
from typing import Optional
from typing import Tuple

from typing_extensions import Final
from typing_extensions import TypedDict

sys.path.append('./')

from apysc._console import loggers
from apysc._file import module_util
from apysc._lint_and_doc import lint_and_doc_hash_util

logger: Logger = loggers.get_info_logger()


class LintCommand(TypedDict):
    command: str
    lint_name: str


_PY_FILE_DIRS_STR: str = './apysc/ ./tests/ ./test_projects/ ./scripts/'

FLAKE8_NO_PATH_COMMAND: Final[str] = (
    'flake8 --ignore E402,W503'
)

FLAKE8_COMMAND: Final[str] = (
    f'{FLAKE8_NO_PATH_COMMAND} {_PY_FILE_DIRS_STR}'
)

NUMDOCLINT_NO_PATH_COMMAND: Final[str] = (
    'numdoclint -r -f test,sample,_test,_sample,mock_'
)

NUMDOCLINT_COMMAND: Final[str] = (
    f'{NUMDOCLINT_NO_PATH_COMMAND} -p ./'
)

MYPY_NO_PATH_COMMAND: Final[str] = (
    'mypy --ignore-missing-imports --follow-imports skip '
    '--disallow-untyped-calls --disallow-untyped-defs '
    '--strict-optional --strict-equality'
)

MYPY_COMMAND: Final[str] = (
    f'{MYPY_NO_PATH_COMMAND} {_PY_FILE_DIRS_STR}'
)

PYRIGHT_COMMAND: Final[str] = f'pyright {_PY_FILE_DIRS_STR}'

CHECK_APYSC_TOP_LEVEL_IMPORT_COMMAND: Final[str] = (
    'python ./scripts/check_apysc_top_level_import.py'
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
        './scripts/',
    ]
    with mp.Pool(processes=len(dir_paths)) as p:
        module_paths_list: List[List[str]] = p.map(
            func=module_util.get_module_paths_recursively,
            iterable=dir_paths)
    module_paths: List[str] = []
    for module_paths_ in module_paths_list:
        module_paths.extend(module_paths_)
    return module_paths


class _CommandOptions(TypedDict):
    skip_overall_docs_build: bool


def _main() -> None:
    """Entry point of this command.
    """
    from scripts.build_docs import HASHED_VALS_DIR_PATH
    options: _CommandOptions = _get_command_options()
    shutil.rmtree('./build/', ignore_errors=True)
    if not options['skip_overall_docs_build']:
        shutil.rmtree(HASHED_VALS_DIR_PATH, ignore_errors=True)
        _update_doc_files_timestamp()
    _remove_tmp_py_module()

    logger.info(msg='Documentation build started.')
    build_doc_process: sp.Popen = _start_subprocess(
        command_strs=['python', './scripts/build_docs.py'])

    logger.info(msg='numdoclint command started.')
    numdoclint_processes: List[sp.Popen] = _start_numdoclint_processes()

    logger.info(msg='mypy command started.')
    mypy_process: sp.Popen = sp.Popen(
        _MYPY_COMMAND['command'].split(' '), stdout=sp.PIPE, stderr=sp.PIPE)

    logger.info(msg='Pyright command started.')
    pyright_process: sp.Popen = sp.Popen(
        _PYRIGHT_COMMAND['command'].split(' '),
        stdout=sp.PIPE, stderr=sp.PIPE)

    logger.info(msg='Checking apysc top-level importing command started.')
    checking_apysc_top_level_import_process: sp.Popen = sp.Popen(
        CHECK_APYSC_TOP_LEVEL_IMPORT_COMMAND.split(' '),
        stdout=sp.PIPE, stderr=sp.PIPE)

    lint_commands: List[LintCommand]
    updated_module_paths: List[str]
    lint_commands, updated_module_paths, = _make_inplace_lint_commands()
    for lint_command in lint_commands:
        run_lint_command(lint_command=lint_command)
    logger.info(msg='flake8 command started.')
    flake8_process: sp.Popen = _start_subprocess(
        command_strs=_FLAKE8_COMMAND['command'].split(' '))

    hash_lint_types: List[lint_and_doc_hash_util.HashType] = [
        lint_and_doc_hash_util.HashType.AUTOFLAKE,
        lint_and_doc_hash_util.HashType.ISORT,
        lint_and_doc_hash_util.HashType.AUTOPEP8,
    ]
    for hash_lint_type in hash_lint_types:
        logger.info(
            msg=f'Saving {hash_lint_type.value} hash files...')
        lint_and_doc_hash_util.save_target_modules_hash(
            module_paths=updated_module_paths,
            hash_type=hash_lint_type)

    _check_build_doc_process(build_doc_process=build_doc_process)
    _check_flake8_process(flake8_process=flake8_process)
    _check_numdoclint_process(numdoclint_processes=numdoclint_processes)
    _check_mypy_process(mypy_process=mypy_process)
    _check_pyright_process(pyright_process=pyright_process)
    _check_apysc_top_level_importing_process(
        process=checking_apysc_top_level_import_process)

    logger.info(msg='Ended.')


_SRC_DOCS_DIR_PATH: str = './docs_src/source/'


def _update_doc_files_timestamp() -> None:
    """
    Update each document timestamp (file updated time)
    to build with the Sphinx.
    """
    file_or_dir_names: List[str] = os.listdir(_SRC_DOCS_DIR_PATH)
    for file_or_dir_name in file_or_dir_names:
        file_or_dir_path: str = os.path.join(
            _SRC_DOCS_DIR_PATH, file_or_dir_name,
        )
        if os.path.isdir(file_or_dir_path):
            continue
        if not file_or_dir_path.endswith('.md'):
            continue
        now_unix_time: float = datetime.now().timestamp()
        os.utime(file_or_dir_path, (now_unix_time, now_unix_time))


def _start_numdoclint_processes() -> List[sp.Popen]:
    """
    Start numdoclint subprocesses.

    Returns
    -------
    numdoclint_processes : list of Popen
        Started subprocesses.
    """
    paths: List[str] = [
        './apysc/', './tests/', './test_projects/', './scripts/',
    ]
    numdoclint_processes: List[sp.Popen] = []
    for path in paths:
        command_strs: List[str] = NUMDOCLINT_NO_PATH_COMMAND.split(' ')
        if not path.endswith('/'):
            command_strs.remove('-r')
        command_strs.extend(['-p', f'{path}'])
        process: sp.Popen = _start_subprocess(
            command_strs=command_strs)
        numdoclint_processes.append(process)
    return numdoclint_processes


class _ApyscTopLevelImportingError(Exception):
    pass


def _check_apysc_top_level_importing_process(process: sp.Popen) -> None:
    """
    Check the apysc top-level import checking process result.

    Parameters
    ----------
    process : Popen
        Target checking command process.

    Raises
    ------
    _ApyscTopLevelImportingError
        If there is an error in the command output.
    """
    print('-' * 20)
    stdout: bytes
    logger.info(
        msg='Waiting apysc top-level import checking command completion...')
    stdout, _ = process.communicate()
    stdout_str: str = stdout.decode()
    lines: List[str] = stdout_str.splitlines()
    print(stdout_str)
    for line in lines:
        if 'Traceback' not in line:
            continue
        raise _ApyscTopLevelImportingError(
            f'There is a invalid top-level apysc import: \n{stdout_str}')


class _PyrightError(Exception):
    pass


def _check_pyright_process(pyright_process: sp.Popen) -> None:
    """
    Check the Pyright command process result.

    Parameters
    ----------
    pyright_process : Popen
        Target Pyright command process.

    Raises
    ------
    _PyrightError
        If there is a Pyright error.
    """
    print('-' * 20)
    stdout: bytes
    logger.info(msg='Waiting Pyright command completion...')
    stdout, _ = pyright_process.communicate()
    stdout_str: str = stdout.decode()
    lines: List[str] = stdout_str.splitlines()
    print(stdout_str)
    for line in lines:
        if line.startswith('0 errors'):
            return
    raise _PyrightError(f'There is a Pyright error: \n{stdout_str}')


class _MypyError(Exception):
    pass


def _check_mypy_process(mypy_process: sp.Popen) -> None:
    """
    Check the mypy command process result.

    Parameters
    ----------
    mypy_process : Popen
        Target mypy command process.

    Raises
    ------
    _MypyError
        If there is a mypy error.
    """
    print('-' * 20)
    stdout: bytes
    logger.info(msg='Waiting mypy command completion...')
    stdout, _ = mypy_process.communicate()
    stdout_str: str = stdout.decode().lower().strip()
    print(stdout_str)
    if 'error' not in stdout_str:
        return
    raise _MypyError(f'There is a mypy error: \n{stdout_str}')


class _NumdoclintError(Exception):
    pass


def _check_numdoclint_process(
        numdoclint_processes: List[sp.Popen]) -> None:
    """
    Check the numdoclint command process result.

    Parameters
    ----------
    numdoclint_processes : list of Popen
        Target numdoclint command processes.

    Raises
    ------
    _NumdoclintError
        If there is a numdoclint error.
    """
    stdout: bytes
    logger.info(msg='Waiting numdoclint command completion...')
    for numdoclint_process in numdoclint_processes:
        stdout, _ = numdoclint_process.communicate()
        stdout_str: str = stdout.decode().replace('[]', '').strip()
        if stdout_str == '':
            continue
        raise _NumdoclintError(f'There is a numdoclint error: \n{stdout_str}')


class _Flake8Error(Exception):
    pass


def _check_flake8_process(flake8_process: sp.Popen) -> None:
    """
    Check the flake8 command process result.

    Parameters
    ----------
    flake8_process : Popen
        Target flake8 command process.

    Raises
    ------
    _Flake8Error
        If there is a flake8 error.
    """
    stdout: bytes
    logger.info(msg='Waiting flake8 command completion...')
    stdout, _ = flake8_process.communicate()
    stdout_str: str = stdout.decode().strip()
    if stdout_str == '':
        return
    raise _Flake8Error(f'There is a flake8 command error:\n{stdout_str}')


class _DocumentBuildError(Exception):
    pass


def _check_build_doc_process(build_doc_process: sp.Popen) -> None:
    """
    Check the documentation build process result.

    Parameters
    ----------
    build_doc_process : Popen
        Target documentation build process.

    Raises
    ------
    _DocumentBuildError
        If there is a documentation build error.
    """
    stdout: bytes
    logger.info(msg='Waiting documentation build completion...')
    stdout, _ = build_doc_process.communicate()
    stdout_str: str = stdout.decode()
    if 'Traceback' not in stdout_str:
        return
    raise _DocumentBuildError(
        f'There is a document build error: {stdout_str}')


def _start_subprocess(command_strs: List[str]) -> sp.Popen:
    """
    Start a subprocess with the specified command.

    Parameters
    ----------
    command_strs : list of str
        Target command strings.

    Returns
    -------
    process : Popen
        Created subprocess object.
    """
    process: sp.Popen = sp.Popen(
        command_strs, stdout=sp.PIPE, stderr=sp.STDOUT)
    return process


_FLAKE8_COMMAND: LintCommand = {
    'command': FLAKE8_COMMAND,
    'lint_name': 'flake8',
}

_MYPY_COMMAND: LintCommand = {
    'command': MYPY_COMMAND,
    'lint_name': 'mypy',
}

_PYRIGHT_COMMAND: LintCommand = {
    'command': PYRIGHT_COMMAND,
    'lint_name': 'Pyright',
}


def _make_inplace_lint_commands() -> Tuple[List[LintCommand], List[str]]:
    """
    Make the in-place lint commands (autoflake, isort, and autopep8) list.

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
    isort_updated_module_paths: List[str] = lint_and_doc_hash_util.\
        remove_not_updated_module_paths(
            module_paths=module_paths,
            hash_type=lint_and_doc_hash_util.HashType.ISORT)
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
    autopep8_updated_module_paths: List[str] = lint_and_doc_hash_util.\
        remove_not_updated_module_paths(
            module_paths=module_paths,
            hash_type=lint_and_doc_hash_util.HashType.AUTOPEP8)
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
    autoflake_updated_module_paths: List[str] = lint_and_doc_hash_util.\
        remove_not_updated_module_paths(
            module_paths=module_paths,
            hash_type=lint_and_doc_hash_util.HashType.AUTOFLAKE)
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
