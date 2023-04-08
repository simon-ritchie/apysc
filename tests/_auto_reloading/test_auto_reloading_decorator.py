import os
import apysc as ap
import shutil
from datetime import datetime, timedelta
import time

from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings, assert_raises
from apysc._auto_reloading import auto_reloading_decorator
from apysc._file import file_util


@apply_test_settings()
def test__are_files_updated() -> None:
    test_root_dir_path: str = os.path.join(
        "tmp/test_auto_reloading_decorator_1/"
    )
    shutil.rmtree(test_root_dir_path, ignore_errors=True)
    test_subdir_path: str = os.path.join(test_root_dir_path, "subdir/")
    os.makedirs(test_subdir_path, exist_ok=True)
    file_path_1: str = os.path.join(test_root_dir_path, "test_1.py")
    file_util.save_plain_txt(
        txt="print(10)",
        file_path=file_path_1,
    )
    file_path_2: str = os.path.join(test_subdir_path, "test_2.py")
    file_util.save_plain_txt(
        txt="print(20)",
        file_path=file_path_2,
    )
    file_path_3: str = os.path.join(test_root_dir_path, "test_3.txt")
    file_util.save_plain_txt(
        txt="Test",
        file_path=file_path_3,
    )

    now: datetime = datetime.now()
    last_executed_time: datetime = now + timedelta(minutes=3)
    result: bool = auto_reloading_decorator._are_files_updated(
        last_executed_time=last_executed_time,
        checking_dir_paths=[test_root_dir_path],
    )
    assert not result

    last_executed_time: datetime = now + timedelta(minutes=-3)
    result = auto_reloading_decorator._are_files_updated(
        last_executed_time=last_executed_time,
        checking_dir_paths=[test_root_dir_path],
    )
    assert result

    file_util.delete_file_if_exists(file_path=file_path_1)
    result = auto_reloading_decorator._are_files_updated(
        last_executed_time=last_executed_time,
        checking_dir_paths=[test_root_dir_path],
    )
    assert result

    file_util.delete_file_if_exists(file_path=file_path_2)
    result = auto_reloading_decorator._are_files_updated(
        last_executed_time=last_executed_time,
        checking_dir_paths=[test_root_dir_path],
    )
    assert not result

    shutil.rmtree(test_root_dir_path, ignore_errors=True)


_count: int = 0


@apply_test_settings()
def test_set_auto_reloading() -> None:
    global _count
    _count = 0
    test_root_dir_path: str = os.path.join(
        "tmp/test_auto_reloading_decorator_2/"
    )
    shutil.rmtree(test_root_dir_path, ignore_errors=True)
    test_file_path: str = os.path.join(test_root_dir_path, "test_file.py")
    os.makedirs(os.path.dirname(test_root_dir_path), exist_ok=True)

    @auto_reloading_decorator.set_auto_reloading(
        checking_dir_paths=[test_root_dir_path],
        max_checking_num=5,
    )
    def _test_func(*, a: int) -> int:
        global _count
        _count += 1

        if _count <= 3:
            file_util.save_plain_txt(txt="print(10)", file_path=test_file_path)
        if _count == 2:
            raise Exception()
        return 200

    result: int = _test_func(a=10)
    assert result == 200
    assert _count == 4

    shutil.rmtree(test_root_dir_path, ignore_errors=True)
