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

_ROOT_MODULE_PATHS_STR: Final[str] = (
    './apply_lints_and_build_docs.py ./build_docs.py ./build.py '
    './run_flake8.py ./run_mypy.py ./run_numdoclint.py ./run_tests.py '
    './setup.py install_released_package.py'
)

FLAKE8_COMMAND: Final[str] = (
    f'{FLAKE8_NO_PATH_COMMAND} ./apysc/ ./tests/ ./test_projects/ '
    f'{_ROOT_MODULE_PATHS_STR}'
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
    f'{MYPY_NO_PATH_COMMAND} ./apysc/ '
    f'./tests/ ./test_projects/ {_ROOT_MODULE_PATHS_STR}'
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
    build_doc_process: sp.Popen = _start_subprocess(
        command_strs=['python', 'build_docs.py'])

    logger.info(msg='numdoclint command started.')
    numdoclint_processes: List[sp.Popen] = _start_numdoclint_processes()

    logger.info(msg='mypy command started.')
    mypy_process: sp.Popen = sp.Popen(
        _MYPY_COMMAND['command'].split(' '), stdout=sp.PIPE, stderr=sp.PIPE)

    lint_commands: List[LintCommand]
    updated_module_paths: List[str]
    lint_commands, updated_module_paths, = _make_inplace_lint_commands()
    for lint_command in lint_commands:
        run_lint_command(lint_command=lint_command)
    logger.info(msg='flake8 command started.')
    flake8_process: sp.Popen = _start_subprocess(
        command_strs=_FLAKE8_COMMAND['command'].split(' '))

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

    _check_build_doc_process(build_doc_process=build_doc_process)
    _check_flake8_process(flake8_process=flake8_process)
    _check_numdoclint_process(numdoclint_processes=numdoclint_processes)
    _check_mypy_process(mypy_process=mypy_process)

    logger.info(msg='Ended.')


def _start_numdoclint_processes() -> List[sp.Popen]:
    """
    Start numdoclint subprocesses.

    Returns
    -------
    numdoclint_processes : list of Popen
        Started subprocesses.
    """
    dir_paths: List[str] = [
        './apysc/', './tests/', './test_projects/',
    ]
    numdoclint_processes: List[sp.Popen] = []
    for dir_path in dir_paths:
        command_strs: List[str] = NUMDOCLINT_NO_PATH_COMMAND.split(' ')
        command_strs.extend(['-p', f'{dir_path}'])
        process: sp.Popen = _start_subprocess(
            command_strs=command_strs)
        numdoclint_processes.append(process)
    return numdoclint_processes


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
        print(stdout_str)
        if stdout_str == '':
            return
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
    print(stdout_str)
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
    stderr: bytes
    logger.info(msg='Waiting documentation build completion...')
    stdout, stderr = build_doc_process.communicate()
    stdout_str: str = stdout.decode()
    stderr_str: str = stderr.decode()
    for string in (stdout_str, stderr_str):
        if 'Traceback' not in string:
            continue
        raise _DocumentBuildError(
            f'There is a document build error: {string}')


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
    process: sp.Popen = sp.Popen(command_strs, stdout=sp.PIPE, stderr=sp.PIPE)
    return process


_FLAKE8_COMMAND: LintCommand = {
    'command': FLAKE8_COMMAND,
    'lint_name': 'flake8',
}

_NUMDOCLINT_COMMAND: LintCommand = {
    'command': NUMDOCLINT_COMMAND,
    'lint_name': 'numdoclint',
}

_MYPY_COMMAND: LintCommand = {
    'command': MYPY_COMMAND,
    'lint_name': 'mypy',
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
