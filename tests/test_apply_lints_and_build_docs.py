import os
from random import randint
from typing import List

from retrying import retry

import apply_lints_and_build_docs
from apply_lints_and_build_docs import LintCommand
from apysc._file import file_util
from apysc._lint.lint_hash_util import LintType


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
def test__make_lint_commands() -> None:
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
    autoflake_updated_module_paths: List[str]
    autopep8_updated_module_paths: List[str]
    lint_commands, autoflake_updated_module_paths, \
        autopep8_updated_module_paths = \
        apply_lints_and_build_docs._make_lint_commands()
    lint_names: List[str] = [
        lint_command['lint_name'] for lint_command in lint_commands]
    assert lint_names == [
        'autoflake',
        'isort',
        'autopep8',
        'flake8',
        'numdoclint',
        'mypy',
    ]
    assert autoflake_updated_module_paths == ['./apysc/_display/sprite.py']
    assert autopep8_updated_module_paths == ['./apysc/_display/sprite.py']

    def mock_remove_not_updated_module_paths_2(
            module_paths: List[str],
            lint_type: LintType) -> List[str]:
        return []

    apply_lints_and_build_docs.lint_hash_util.\
        remove_not_updated_module_paths = \
        mock_remove_not_updated_module_paths_2
    lint_commands, autoflake_updated_module_paths, \
        autopep8_updated_module_paths = \
        apply_lints_and_build_docs._make_lint_commands()
    lint_names = [
        lint_command['lint_name'] for lint_command in lint_commands]
    assert lint_names == [
        'isort',
        'flake8',
        'numdoclint',
        'mypy',
    ]
    assert autopep8_updated_module_paths == []

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
