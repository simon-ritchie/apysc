import os
from typing import List

from apysc._file import file_util
from apysc._lint_and_doc import lint_and_doc_hash_util
from apysc._lint_and_doc.lint_and_doc_hash_util import HashType
from apysc._lint_and_doc.lint_and_doc_hash_util import _IsFileUpdatedArgs
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_get_lint_hash_dir_path() -> None:
    dir_path: str = lint_and_doc_hash_util.get_hash_dir_path(hash_type=HashType.ISORT)
    assert dir_path == ("./.lint_and_doc_hash/.isort/")
    assert os.path.isdir(dir_path)


@apply_test_settings()
def test_get_target_file_hash_file_path() -> None:
    file_path: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
        file_path="./apysc/_display/sprite.py", hash_type=HashType.ISORT
    )
    expected: str = "./.lint_and_doc_hash/.isort/apysc/_display/sprite"
    assert file_path == expected
    assert os.path.isdir(os.path.dirname(file_path))


@apply_test_settings()
def test_read_target_file_hash() -> None:
    file_util.remove_file_if_exists(
        file_path="./apysc/_display/not_existing_module_1.py"
    )
    hashed_string: str = lint_and_doc_hash_util.read_target_file_hash(
        file_path="./apysc/_display/not_existing_module_1.py"
    )
    assert hashed_string == ""

    hashed_string = lint_and_doc_hash_util.read_target_file_hash(
        file_path="./apysc/_display/sprite.py"
    )
    assert hashed_string != ""


@apply_test_settings()
def test_read_saved_hash() -> None:
    module_path: str = "./apysc/_display/not_existing_module_2.py"
    file_path: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
        file_path=module_path, hash_type=HashType.ISORT
    )
    file_util.remove_file_if_exists(file_path=file_path)

    saved_hash: str = lint_and_doc_hash_util.read_saved_hash(
        file_path=module_path, hash_type=HashType.ISORT
    )
    assert saved_hash == ""

    file_util.save_plain_txt(txt="abcdef", file_path=file_path)
    saved_hash = lint_and_doc_hash_util.read_saved_hash(
        file_path=module_path, hash_type=HashType.ISORT
    )
    assert saved_hash == "abcdef"

    file_util.remove_file_if_exists(file_path=file_path)


@apply_test_settings()
def test_save_target_file_hash() -> None:
    module_path: str = "./apysc/_display/not_existing_module_3.py"
    hash_path: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
        file_path=module_path, hash_type=HashType.ISORT
    )
    file_util.remove_file_if_exists(file_path=module_path)
    file_util.remove_file_if_exists(file_path=hash_path)

    lint_and_doc_hash_util.save_target_file_hash(
        file_path=module_path, hash_type=HashType.ISORT
    )
    saved_hash: str = lint_and_doc_hash_util.read_saved_hash(
        file_path=module_path, hash_type=HashType.ISORT
    )
    assert saved_hash == ""

    file_util.save_plain_txt(txt="abcdef", file_path=module_path)
    lint_and_doc_hash_util.save_target_file_hash(
        file_path=module_path, hash_type=HashType.ISORT
    )
    saved_hash = lint_and_doc_hash_util.read_saved_hash(
        file_path=module_path, hash_type=HashType.ISORT
    )
    assert saved_hash != ""

    file_util.remove_file_if_exists(file_path=module_path)
    file_util.remove_file_if_exists(file_path=hash_path)


@apply_test_settings()
def test_is_file_updated() -> None:
    module_path: str = "./apysc/_display/not_existing_module_4.py"
    hash_path: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
        file_path=module_path, hash_type=HashType.ISORT
    )
    file_util.remove_file_if_exists(file_path=module_path)
    file_util.remove_file_if_exists(file_path=hash_path)

    result: bool = lint_and_doc_hash_util.is_file_updated(
        file_path=module_path, hash_type=HashType.ISORT
    )
    assert not result

    file_util.save_plain_txt(txt="abc", file_path=module_path)
    result = lint_and_doc_hash_util.is_file_updated(
        file_path=module_path, hash_type=HashType.ISORT
    )
    assert result

    lint_and_doc_hash_util.save_target_file_hash(
        file_path=module_path, hash_type=HashType.ISORT
    )
    result = lint_and_doc_hash_util.is_file_updated(
        file_path=module_path, hash_type=HashType.ISORT
    )
    assert not result

    file_util.remove_file_if_exists(file_path=module_path)
    file_util.remove_file_if_exists(file_path=hash_path)


@apply_test_settings()
def test__is_file_updated_func_for_multiprocessing() -> None:
    module_path: str = "./apysc/_display/not_existing_module_5.py"
    file_util.remove_file_if_exists(file_path=module_path)

    args: _IsFileUpdatedArgs = {
        "file_path": module_path,
        "hash_type": HashType.ISORT,
    }
    result: bool = lint_and_doc_hash_util._is_file_updated_func_for_multiprocessing(
        args=args
    )
    assert not result

    file_util.save_plain_txt(txt="abc", file_path=module_path)
    result = lint_and_doc_hash_util._is_file_updated_func_for_multiprocessing(args=args)
    assert result

    file_util.remove_file_if_exists(file_path=module_path)


@apply_test_settings()
def test__create_args_list_for_multiprocessing() -> None:
    args_list: List[
        _IsFileUpdatedArgs
    ] = lint_and_doc_hash_util._create_args_list_for_multiprocessing(
        file_paths=[
            "test/path_1.py",
            "test/path_2.py",
        ],
        hash_type=HashType.ISORT,
    )
    assert args_list == [
        {
            "file_path": "test/path_1.py",
            "hash_type": HashType.ISORT,
        },
        {
            "file_path": "test/path_2.py",
            "hash_type": HashType.ISORT,
        },
    ]


@apply_test_settings()
def test_remove_not_updated_file_paths() -> None:
    module_path: str = "./apysc/_display/not_existing_module_6.py"
    hash_path: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
        file_path=module_path, hash_type=HashType.ISORT
    )
    file_util.remove_file_if_exists(file_path=module_path)
    file_util.remove_file_if_exists(file_path=hash_path)

    file_util.save_plain_txt(txt="abc", file_path=module_path)
    sliced_module_paths: List[
        str
    ] = lint_and_doc_hash_util.remove_not_updated_file_paths(
        file_paths=[module_path], hash_type=HashType.ISORT
    )
    assert sliced_module_paths == [module_path]

    lint_and_doc_hash_util.save_target_file_hash(
        file_path=module_path, hash_type=HashType.ISORT
    )
    sliced_module_paths = lint_and_doc_hash_util.remove_not_updated_file_paths(
        file_paths=[module_path], hash_type=HashType.ISORT
    )
    assert sliced_module_paths == []

    file_util.remove_file_if_exists(file_path=module_path)
    file_util.remove_file_if_exists(file_path=hash_path)


@apply_test_settings()
def test_save_target_files_hash() -> None:
    module_path_1: str = "./apysc/_display/not_existing_module_7.py"
    module_path_2: str = "./apysc/_display/not_existing_module_8.py"
    hash_path_1: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
        file_path=module_path_1, hash_type=HashType.ISORT
    )
    hash_path_2: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
        file_path=module_path_2, hash_type=HashType.ISORT
    )
    file_util.remove_file_if_exists(file_path=module_path_1)
    file_util.remove_file_if_exists(file_path=hash_path_1)
    file_util.remove_file_if_exists(file_path=module_path_2)
    file_util.remove_file_if_exists(file_path=hash_path_2)

    file_util.save_plain_txt(txt="abc", file_path=module_path_1)
    file_util.save_plain_txt(txt="def", file_path=module_path_2)
    lint_and_doc_hash_util.save_target_files_hash(
        file_paths=[module_path_1, module_path_2], hash_type=HashType.ISORT
    )
    hash_1: str = lint_and_doc_hash_util.read_saved_hash(
        file_path=module_path_1, hash_type=HashType.ISORT
    )
    hash_2: str = lint_and_doc_hash_util.read_saved_hash(
        file_path=module_path_2, hash_type=HashType.ISORT
    )
    assert hash_1 != ""
    assert hash_2 != ""

    file_util.remove_file_if_exists(file_path=module_path_1)
    file_util.remove_file_if_exists(file_path=hash_path_1)
    file_util.remove_file_if_exists(file_path=module_path_2)
    file_util.remove_file_if_exists(file_path=hash_path_2)


@apply_test_settings()
def test_delete_target_file_hash() -> None:
    file_path: str = "./apysc/_display/circle.py"
    hash_file_path: str = lint_and_doc_hash_util.get_target_file_hash_file_path(
        file_path=file_path,
        hash_type=HashType.ISORT,
    )
    lint_and_doc_hash_util.delete_target_file_hash(
        file_path=file_path,
        hash_type=HashType.ISORT,
    )
    assert not os.path.exists(hash_file_path)

    os.system(f"git checkout {hash_file_path}")
