import os
import shutil
import subprocess as sp
import time
from random import randint
from typing import List

from retrying import retry

import apply_lints_and_build_docs
from apply_lints_and_build_docs import LintCommand
from apysc._file import file_util
from apysc._lint.lint_hash_util import LintType
from tests.testing_helper import assert_raises


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_run_lint_command() -> None:
    lint_command: LintCommand = {
        'command': 'ls -l',
        'lint_name': 'test',
    }
    stdout: str = apply_lints_and_build_docs.run_lint_command(
        lint_command=lint_command)
    assert 'apysc' in stdout


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__remove_tmp_py_module() -> None:
    file_util.save_plain_txt(txt='\n', file_path='./tmp_123.py')
    apply_lints_and_build_docs._remove_tmp_py_module()
    assert not os.path.exists('./tmp_123.py')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_run_command() -> None:
    stdout: str = apply_lints_and_build_docs.run_command(command='ls')
    assert 'apysc' in stdout


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_root_dir_module_paths() -> None:
    module_paths: List[str] = apply_lints_and_build_docs.\
        _get_root_dir_module_paths()
    expected_paths: List[str] = [
        './apply_lints_and_build_docs.py',
        './build.py',
    ]
    for expected in expected_paths:
        assert expected in module_paths

    unexpected_paths: List[str] = [
        './__init__.py',
        './apysc',
        './requirements.txt',
        './tmp.py',
    ]
    for unexpected in unexpected_paths:
        assert unexpected not in module_paths


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_module_paths() -> None:
    module_paths: List[str] = apply_lints_and_build_docs._get_module_paths()
    expected_paths: List[str] = [
        './apysc/_display/sprite.py',
        './docs_src/source/conf.py',
        './tests/_display/test_sprite.py',
        './test_projects/draw_rect/main.py',
        './build.py',
    ]
    for expected in expected_paths:
        assert expected in module_paths
        assert expected.endswith('.py')


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__make_inplace_lint_commands() -> None:
    original_remove_not_updated_module_paths_func = \
        apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths

    def mock_remove_not_updated_module_paths_1(
            module_paths: List[str],
            lint_type: LintType) -> List[str]:
        return ['./apysc/_display/sprite.py']

    apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths = \
        mock_remove_not_updated_module_paths_1

    lint_commands: List[LintCommand]
    updated_module_paths: List[str]
    lint_commands, updated_module_paths = \
        apply_lints_and_build_docs._make_inplace_lint_commands()
    lint_names: List[str] = [
        lint_command['lint_name'] for lint_command in lint_commands]
    assert lint_names == [
        'autoflake',
        'isort',
        'autopep8',
    ]
    assert updated_module_paths == ['./apysc/_display/sprite.py']

    def mock_remove_not_updated_module_paths_2(
            module_paths: List[str],
            lint_type: LintType) -> List[str]:
        return []

    apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths = \
        mock_remove_not_updated_module_paths_2
    lint_commands, updated_module_paths = \
        apply_lints_and_build_docs._make_inplace_lint_commands()
    lint_names = [
        lint_command['lint_name'] for lint_command in lint_commands]
    assert lint_names == []
    assert updated_module_paths == []

    apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths = \
        original_remove_not_updated_module_paths_func


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_joined_paths_str() -> None:
    joined_paths_str: str = apply_lints_and_build_docs._get_joined_paths_str(
        module_paths=['./test/path_1.py', './test/path_2.py'])
    assert joined_paths_str == (
        './test/path_1.py ./test/path_2.py'
    )


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_autoflake_lint_command_if_module_updated() -> None:
    original_remove_not_updated_module_paths_func = \
        apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths

    def mock_remove_not_updated_module_paths_1(
            module_paths: List[str],
            lint_type: LintType) -> List[str]:
        return []

    apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths = \
        mock_remove_not_updated_module_paths_1
    lint_commands: List[LintCommand] = []
    module_paths: List[str] = ['./apysc/_display/sprite.py']
    autoflake_updated_module_paths: List[str] = apply_lints_and_build_docs.\
        _append_autoflake_lint_command_if_module_updated(
            lint_commands=lint_commands, module_paths=module_paths)
    assert lint_commands == []
    assert autoflake_updated_module_paths == []

    def mock_remove_not_updated_module_paths_2(
            module_paths: List[str],
            lint_type: LintType) -> List[str]:
        return ['./apysc/_display/sprite.py']

    apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths = \
        mock_remove_not_updated_module_paths_2
    autoflake_updated_module_paths = apply_lints_and_build_docs.\
        _append_autoflake_lint_command_if_module_updated(
            lint_commands=lint_commands, module_paths=module_paths)
    assert len(lint_commands) == 1
    assert lint_commands[0]['lint_name'] == 'autoflake'
    assert autoflake_updated_module_paths == ['./apysc/_display/sprite.py']

    apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths = \
        original_remove_not_updated_module_paths_func


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_autopep8_lint_command_if_module_updated() -> None:
    original_remove_not_updated_module_paths_func = \
        apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths

    def mock_remove_not_updated_module_paths_1(
            module_paths: List[str],
            lint_type: LintType) -> List[str]:
        return []

    apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths = \
        mock_remove_not_updated_module_paths_1
    lint_commands: List[LintCommand] = []
    module_paths: List[str] = ['./apysc/_display/sprite.py']
    autopep8_updated_module_paths: List[str] = apply_lints_and_build_docs.\
        _append_autopep8_lint_command_if_module_updated(
            lint_commands=lint_commands, module_paths=module_paths)
    assert lint_commands == []
    assert autopep8_updated_module_paths == []

    def mock_remove_not_updated_module_paths_2(
            module_paths: List[str],
            lint_type: LintType) -> List[str]:
        return ['./apysc/_display/sprite.py']

    apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths = \
        mock_remove_not_updated_module_paths_2
    autopep8_updated_module_paths = apply_lints_and_build_docs.\
        _append_autopep8_lint_command_if_module_updated(
            lint_commands=lint_commands, module_paths=module_paths)
    assert len(lint_commands) == 1
    assert lint_commands[0]['lint_name'] == 'autopep8'
    assert autopep8_updated_module_paths == ['./apysc/_display/sprite.py']

    apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths = \
        original_remove_not_updated_module_paths_func


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_isort_lint_command_if_module_updated() -> None:
    original_remove_not_updated_module_paths_func = \
        apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths

    def mock_remove_not_updated_module_paths_1(
            module_paths: List[str],
            lint_type: LintType) -> List[str]:
        return []

    apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths = \
        mock_remove_not_updated_module_paths_1
    lint_commands: List[LintCommand] = []
    module_paths: List[str] = ['./apysc/_display/sprite.py']
    isort_updated_module_paths: List[str] = apply_lints_and_build_docs.\
        _append_isort_lint_command_if_module_updated(
            lint_commands=lint_commands, module_paths=module_paths)
    assert lint_commands == []
    assert isort_updated_module_paths == []

    def mock_remove_not_updated_module_paths_2(
            module_paths: List[str],
            lint_type: LintType) -> List[str]:
        return ['./apysc/_display/sprite.py']

    apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths = \
        mock_remove_not_updated_module_paths_2
    isort_updated_module_paths = apply_lints_and_build_docs.\
        _append_isort_lint_command_if_module_updated(
            lint_commands=lint_commands, module_paths=module_paths)
    assert len(lint_commands) == 1
    assert lint_commands[0]['lint_name'] == 'isort'
    assert isort_updated_module_paths == ['./apysc/_display/sprite.py']

    apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths = \
        original_remove_not_updated_module_paths_func


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__start_subprocess() -> None:
    process: sp.Popen = apply_lints_and_build_docs._start_subprocess(
        command_strs=['ls', '-l'])
    stdout: bytes
    stdout, _ = process.communicate()
    assert 'apysc' in stdout.decode()


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__check_build_doc_process() -> None:
    build_doc_process: sp.Popen = \
        apply_lints_and_build_docs._start_subprocess(
            command_strs=['python', '-c', 'print("build completed!")'])
    apply_lints_and_build_docs._check_build_doc_process(
        build_doc_process=build_doc_process)

    build_doc_process = apply_lints_and_build_docs._start_subprocess(
        command_strs=['python', '-c', 'raise Exception("Build failed!")'])
    assert_raises(
        expected_error_class=apply_lints_and_build_docs._DocumentBuildError,
        func_or_method=apply_lints_and_build_docs._check_build_doc_process,
        kwargs={'build_doc_process': build_doc_process})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__check_flake8_process() -> None:
    flake8_process: sp.Popen = apply_lints_and_build_docs._start_subprocess(
        command_strs=['python', '-c', '"x = 1 + 1"'])
    apply_lints_and_build_docs._check_flake8_process(
        flake8_process=flake8_process)

    flake8_process = apply_lints_and_build_docs._start_subprocess(
        command_strs=[
            'python', '-c', 'print("F401 module imported but unused")'])
    assert_raises(
        expected_error_class=apply_lints_and_build_docs._Flake8Error,
        func_or_method=apply_lints_and_build_docs._check_flake8_process,
        kwargs={'flake8_process': flake8_process})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__check_numdoclint_process() -> None:
    numdoclint_process: sp.Popen = \
        apply_lints_and_build_docs._start_subprocess(
            command_strs=['python', '-c', 'print("[]")'])
    apply_lints_and_build_docs._check_numdoclint_process(
        numdoclint_processes=[numdoclint_process])

    numdoclint_process = apply_lints_and_build_docs._start_subprocess(
        command_strs=['python', '-c', 'print("[...]")'])
    assert_raises(
        expected_error_class=apply_lints_and_build_docs._NumdoclintError,
        func_or_method=apply_lints_and_build_docs._check_numdoclint_process,
        kwargs={'numdoclint_processes': [numdoclint_process]})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__check_mypy_process() -> None:
    mypy_process: sp.Popen = apply_lints_and_build_docs._start_subprocess(
        command_strs=[
            'python', '-c',
            'print("Success: no issues found in 710 source files")'])
    apply_lints_and_build_docs._check_mypy_process(mypy_process=mypy_process)

    mypy_process = apply_lints_and_build_docs._start_subprocess(
        command_strs=[
            'python', '-c',
            'print("Found 1 error in 1 file (checked 710 source files)")'])
    assert_raises(
        expected_error_class=apply_lints_and_build_docs._MypyError,
        func_or_method=apply_lints_and_build_docs._check_mypy_process,
        kwargs={'mypy_process': mypy_process})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__start_numdoclint_processes() -> None:
    numdoclint_processes: List[sp.Popen] = apply_lints_and_build_docs.\
        _start_numdoclint_processes()
    assert len(numdoclint_processes) >= 3
    joined_commands: List[str] = [
        str(process.args) for process in numdoclint_processes]
    assert len(set(joined_commands)) == len(joined_commands)
    for joined_command in joined_commands:
        assert 'numdoclint' in joined_command


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__update_doc_files_timestamp() -> None:
    original_src_doc_dir_path: str = \
        apply_lints_and_build_docs._SRC_DOCS_DIR_PATH
    tmp_dir_path: str = './tmp/test_apply_lints_and_build_docs/'
    apply_lints_and_build_docs._SRC_DOCS_DIR_PATH = tmp_dir_path
    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    os.makedirs(tmp_dir_path, exist_ok=True)
    subdir_path: str = os.path.join(
        tmp_dir_path, 'subdir/'
    )
    os.makedirs(subdir_path, exist_ok=True)
    tmp_file_path_1: str = os.path.join(
        tmp_dir_path, 'tmp_1.md',
    )
    tmp_file_path_2: str = os.path.join(
        tmp_dir_path, 'tmp_2.py',
    )
    tmp_file_path_3: str = os.path.join(
        subdir_path, 'tmp_3.md',
    )
    for tmp_file_path in (
            tmp_file_path_1, tmp_file_path_2, tmp_file_path_3):
        with open(tmp_file_path, 'w') as f:
            f.write('')
    pre_tmp_file_path_1_mtime: float = os.path.getmtime(tmp_file_path_1)
    pre_tmp_file_path_2_mtime: float = os.path.getmtime(tmp_file_path_2)
    pre_tmp_file_path_3_mtime: float = os.path.getmtime(tmp_file_path_3)
    time.sleep(1)
    apply_lints_and_build_docs._update_doc_files_timestamp()
    after_tmp_file_path_1_mtime: float = os.path.getmtime(tmp_file_path_1)
    after_tmp_file_path_2_mtime: float = os.path.getmtime(tmp_file_path_2)
    after_tmp_file_path_3_mtime: float = os.path.getmtime(tmp_file_path_3)
    assert after_tmp_file_path_1_mtime > pre_tmp_file_path_1_mtime
    assert after_tmp_file_path_2_mtime == pre_tmp_file_path_2_mtime
    assert after_tmp_file_path_3_mtime == pre_tmp_file_path_3_mtime

    apply_lints_and_build_docs._SRC_DOCS_DIR_PATH = original_src_doc_dir_path
    shutil.rmtree(tmp_dir_path, ignore_errors=True)
