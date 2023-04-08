import os
import apysc as ap
import shutil
from datetime import datetime, timedelta

from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings, assert_raises
from apysc._auto_reloading import auto_reloading_decorator
from apysc._file import file_util


@apply_test_settings()
def test__are_files_updated() -> None:
    test_root_dir_path: str = os.path.join(
        "tmp/test_auto_reloading_decorator/"
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

    now: datetime = datetime.now()
    last_checked_time: datetime = now + timedelta(minutes=3)
    result: bool = auto_reloading_decorator._are_files_updated(
        last_checked_time=last_checked_time,
        checking_dir_paths=[test_root_dir_path],
    )
    assert not result

    last_checked_time: datetime = now + timedelta(minutes=-3)
    result = auto_reloading_decorator._are_files_updated(
        last_checked_time=last_checked_time,
        checking_dir_paths=[test_root_dir_path],
    )
    assert result

    file_util.delete_file_if_exists(file_path=file_path_1)
    result = auto_reloading_decorator._are_files_updated(
        last_checked_time=last_checked_time,
        checking_dir_paths=[test_root_dir_path],
    )
    assert result

    shutil.rmtree(test_root_dir_path, ignore_errors=True)
