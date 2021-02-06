import os
import shutil

from retrying import retry

from apyscript.file import file_util
from tests import testing_helper


def test_empty_directory() -> None:
    tmp_dir_path: str = '../.tmp_apyscript/'
    os.makedirs(tmp_dir_path, exist_ok=True)
    test_file_path: str = os.path.join(tmp_dir_path, 'test.txt')
    testing_helper.make_blank_file(file_path=test_file_path)
    file_util.empty_directory(directory_path=tmp_dir_path)
    assert os.path.isdir(tmp_dir_path)
    assert len(os.listdir(tmp_dir_path)) == 0

    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    file_util.empty_directory(directory_path=tmp_dir_path)
    assert os.path.isdir(tmp_dir_path)

    shutil.rmtree(tmp_dir_path, ignore_errors=True)


def test_read_txt() -> None:
    tmp_file_path: str = '../tmp_apyscript_test_file_util.txt'
    with open(tmp_file_path, 'w') as f:
        f.write('To be, or not to be, that is the question.')
    txt: str = file_util.read_txt(file_path=tmp_file_path)
    assert txt == 'To be, or not to be, that is the question.'
    os.remove(tmp_file_path)


def test_save_plain_txt() -> None:
    tmp_file_path: str = '../tmp_apyscript_test_file_util.txt'
    file_util.save_plain_txt(
        txt='To be, or not to be, that is the question.',
        file_path=tmp_file_path)
    txt: str = file_util.read_txt(file_path=tmp_file_path)
    assert txt == 'To be, or not to be, that is the question.'
    os.remove(tmp_file_path)

    tmp_dir_path: str = '../tmp_apyscript_test_file_util/'
    tmp_file_path: str = os.path.join(tmp_dir_path, 'test.txt')
    shutil.rmtree(tmp_dir_path, ignore_errors=True)
    file_util.save_plain_txt(
        txt='To be, or not to be, that is the question.',
        file_path=tmp_file_path)
    assert os.path.isfile(tmp_file_path)
    shutil.rmtree(tmp_dir_path, ignore_errors=True)


@retry(stop_max_attempt_number=5, wait_fixed=300)
def test_remove_file_if_exists() -> None:
    tmp_file_path: str = '../tmp_apyscript_test_file_util.txt'
    file_util.save_plain_txt(
        txt='To be, or not to be, that is the question.',
        file_path=tmp_file_path)
    file_util.remove_file_if_exists(file_path=tmp_file_path)
    assert not os.path.exists(tmp_file_path)

    file_util.remove_file_if_exists(file_path=tmp_file_path)


def test_get_abs_module_dir_path() -> None:
    abs_module_dir_path: str = file_util.get_abs_module_dir_path(
        module=file_util)
    expected_dir_path: str = '/mnt/action-py-script/apyscript/file/'
    assert abs_module_dir_path == expected_dir_path


def test_get_abs_directory_path_from_file_path() -> None:
    dir_path: str = file_util.get_abs_directory_path_from_file_path(
        file_path='any/dir/path.txt')
    assert dir_path == 'any/dir/'
