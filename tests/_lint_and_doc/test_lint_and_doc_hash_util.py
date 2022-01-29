import os
from random import randint
from typing import List

from retrying import retry

from apysc._file import file_util
from apysc._lint_and_doc import lint_and_doc_hash_util
from apysc._lint_and_doc.lint_and_doc_hash_util import LintType
from apysc._lint_and_doc.lint_and_doc_hash_util import _IsModuleUpdatedArgs


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_lint_hash_dir_path() -> None:
    dir_path: str = lint_and_doc_hash_util.get_lint_hash_dir_path(
        lint_type=LintType.AUTOPEP8)
    assert dir_path == (
        './.lint_and_doc_hash/.autopep8/'
    )
    assert os.path.isdir(dir_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_target_module_hash_file_path() -> None:
    file_path: str = lint_and_doc_hash_util.get_target_module_hash_file_path(
        module_path='./apysc/_display/sprite.py',
        lint_type=LintType.AUTOPEP8)
    expected: str = (
        './.lint_and_doc_hash/.autopep8/apysc/_display/sprite'
    )
    assert file_path == expected
    assert os.path.isdir(os.path.dirname(file_path))


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_read_target_module_hash() -> None:
    file_util.remove_file_if_exists(
        file_path='./apysc/_display/not_existing_module_1.py')
    hashed_string: str = lint_and_doc_hash_util.read_target_module_hash(
        module_path='./apysc/_display/not_existing_module_1.py')
    assert hashed_string == ''

    hashed_string = lint_and_doc_hash_util.read_target_module_hash(
        module_path='./apysc/_display/sprite.py')
    assert hashed_string != ''


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_read_saved_hash() -> None:
    module_path: str = './apysc/_display/not_existing_module_2.py'
    file_path: str = lint_and_doc_hash_util.get_target_module_hash_file_path(
        module_path=module_path,
        lint_type=LintType.AUTOPEP8)
    file_util.remove_file_if_exists(file_path=file_path)

    saved_hash: str = lint_and_doc_hash_util.read_saved_hash(
        module_path=module_path,
        lint_type=LintType.AUTOPEP8)
    assert saved_hash == ''

    file_util.save_plain_txt(txt='abcdef', file_path=file_path)
    saved_hash = lint_and_doc_hash_util.read_saved_hash(
        module_path=module_path,
        lint_type=LintType.AUTOPEP8)
    assert saved_hash == 'abcdef'

    file_util.remove_file_if_exists(file_path=file_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_save_target_module_hash() -> None:
    module_path: str = './apysc/_display/not_existing_module_3.py'
    hash_path: str = lint_and_doc_hash_util.get_target_module_hash_file_path(
        module_path=module_path, lint_type=LintType.AUTOPEP8)
    file_util.remove_file_if_exists(file_path=module_path)
    file_util.remove_file_if_exists(file_path=hash_path)

    lint_and_doc_hash_util.save_target_module_hash(
        module_path=module_path, lint_type=LintType.AUTOPEP8)
    saved_hash: str = lint_and_doc_hash_util.read_saved_hash(
        module_path=module_path, lint_type=LintType.AUTOPEP8)
    assert saved_hash == ''

    file_util.save_plain_txt(txt='abcdef', file_path=module_path)
    lint_and_doc_hash_util.save_target_module_hash(
        module_path=module_path, lint_type=LintType.AUTOPEP8)
    saved_hash = lint_and_doc_hash_util.read_saved_hash(
        module_path=module_path, lint_type=LintType.AUTOPEP8)
    assert saved_hash != ''

    file_util.remove_file_if_exists(file_path=module_path)
    file_util.remove_file_if_exists(file_path=hash_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_module_updated() -> None:
    module_path: str = './apysc/_display/not_existing_module_4.py'
    hash_path: str = lint_and_doc_hash_util.get_target_module_hash_file_path(
        module_path=module_path, lint_type=LintType.AUTOPEP8)
    file_util.remove_file_if_exists(file_path=module_path)
    file_util.remove_file_if_exists(file_path=hash_path)

    result: bool = lint_and_doc_hash_util.is_module_updated(
        module_path=module_path, lint_type=LintType.AUTOPEP8)
    assert not result

    file_util.save_plain_txt(txt='abc', file_path=module_path)
    result = lint_and_doc_hash_util.is_module_updated(
        module_path=module_path, lint_type=LintType.AUTOPEP8)
    assert result

    lint_and_doc_hash_util.save_target_module_hash(
        module_path=module_path, lint_type=LintType.AUTOPEP8)
    result = lint_and_doc_hash_util.is_module_updated(
        module_path=module_path, lint_type=LintType.AUTOPEP8)
    assert not result

    file_util.remove_file_if_exists(file_path=module_path)
    file_util.remove_file_if_exists(file_path=hash_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__is_module_updated_func_for_multiprocessing() -> None:
    module_path: str = './apysc/_display/not_existing_module_5.py'
    file_util.remove_file_if_exists(file_path=module_path)

    args: _IsModuleUpdatedArgs = {
        'module_path': module_path,
        'lint_type': LintType.AUTOPEP8,
    }
    result: bool = lint_and_doc_hash_util._is_module_updated_func_for_multiprocessing(
        args=args)
    assert not result

    file_util.save_plain_txt(txt='abc', file_path=module_path)
    result = lint_and_doc_hash_util._is_module_updated_func_for_multiprocessing(
        args=args)
    assert result

    file_util.remove_file_if_exists(file_path=module_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__create_args_list_for_multiprocessing() -> None:
    args_list: List[_IsModuleUpdatedArgs] = lint_and_doc_hash_util.\
        _create_args_list_for_multiprocessing(
            module_paths=[
                'test/path_1.py',
                'test/path_2.py',
            ],
            lint_type=LintType.AUTOPEP8)
    assert args_list == [{
        'module_path': 'test/path_1.py',
        'lint_type': LintType.AUTOPEP8,
    }, {
        'module_path': 'test/path_2.py',
        'lint_type': LintType.AUTOPEP8,
    }]


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_remove_not_updated_module_paths() -> None:
    module_path: str = './apysc/_display/not_existing_module_6.py'
    hash_path: str = lint_and_doc_hash_util.get_target_module_hash_file_path(
        module_path=module_path, lint_type=LintType.AUTOPEP8)
    file_util.remove_file_if_exists(file_path=module_path)
    file_util.remove_file_if_exists(file_path=hash_path)

    file_util.save_plain_txt(txt='abc', file_path=module_path)
    sliced_module_paths: List[str] = lint_and_doc_hash_util.\
        remove_not_updated_module_paths(
            module_paths=[module_path], lint_type=LintType.AUTOPEP8)
    assert sliced_module_paths == [module_path]

    lint_and_doc_hash_util.save_target_module_hash(
        module_path=module_path, lint_type=LintType.AUTOPEP8)
    sliced_module_paths = lint_and_doc_hash_util.\
        remove_not_updated_module_paths(
            module_paths=[module_path], lint_type=LintType.AUTOPEP8)
    assert sliced_module_paths == []

    file_util.remove_file_if_exists(file_path=module_path)
    file_util.remove_file_if_exists(file_path=hash_path)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_save_target_modules_hash() -> None:
    module_path_1: str = './apysc/_display/not_existing_module_7.py'
    module_path_2: str = './apysc/_display/not_existing_module_8.py'
    hash_path_1: str = lint_and_doc_hash_util.get_target_module_hash_file_path(
        module_path=module_path_1, lint_type=LintType.AUTOPEP8)
    hash_path_2: str = lint_and_doc_hash_util.get_target_module_hash_file_path(
        module_path=module_path_2, lint_type=LintType.AUTOPEP8)
    file_util.remove_file_if_exists(file_path=module_path_1)
    file_util.remove_file_if_exists(file_path=hash_path_1)
    file_util.remove_file_if_exists(file_path=module_path_2)
    file_util.remove_file_if_exists(file_path=hash_path_2)

    file_util.save_plain_txt(txt='abc', file_path=module_path_1)
    file_util.save_plain_txt(txt='def', file_path=module_path_2)
    lint_and_doc_hash_util.save_target_modules_hash(
        module_paths=[module_path_1, module_path_2],
        lint_type=LintType.AUTOPEP8)
    hash_1: str = lint_and_doc_hash_util.read_saved_hash(
        module_path=module_path_1, lint_type=LintType.AUTOPEP8)
    hash_2: str = lint_and_doc_hash_util.read_saved_hash(
        module_path=module_path_2, lint_type=LintType.AUTOPEP8)
    assert hash_1 != ''
    assert hash_2 != ''

    file_util.remove_file_if_exists(file_path=module_path_1)
    file_util.remove_file_if_exists(file_path=hash_path_1)
    file_util.remove_file_if_exists(file_path=module_path_2)
    file_util.remove_file_if_exists(file_path=hash_path_2)
