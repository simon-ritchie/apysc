from random import randint
import shutil
import os

from retrying import retry

from apysc._jupyter import jupyter_util
from apysc import Stage


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_display_on_jupyter() -> None:
    tmp_dest_dir_path: str = '../tmp_test_jupyter_util/'
    shutil.rmtree(tmp_dest_dir_path, ignore_errors=True)

    stage: Stage = Stage()
    jupyter_util.display_on_jupyter(
        stage=stage,
        html_file_name='test_file.html',
        dest_dir_path=tmp_dest_dir_path)
    expected_file_path: str = os.path.join(
        tmp_dest_dir_path, 'test_file.html')
    assert os.path.isfile(expected_file_path)

    shutil.rmtree(tmp_dest_dir_path, ignore_errors=True)
