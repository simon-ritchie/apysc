import os
import shutil
from random import randint

from retrying import retry

from apysc import Stage
from apysc._jupyter import jupyter_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_display_on_jupyter() -> None:
    tmp_dest_dir_path: str = '../tmp_test_jupyter_util_1/'
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


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__save_overall_html() -> None:
    tmp_dest_dir_path: str = '../tmp_test_jupyter_util_2/'
    shutil.rmtree(tmp_dest_dir_path, ignore_errors=True)

    _: Stage = Stage()
    jupyter_util._save_overall_html(
        html_file_name='test_file.html',
        dest_dir_path=tmp_dest_dir_path,
        minify=True)
    expected_file_path: str = os.path.join(
        tmp_dest_dir_path, 'test_file.html')
    assert os.path.isfile(expected_file_path)

    shutil.rmtree(tmp_dest_dir_path, ignore_errors=True)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_display_on_colaboratory() -> None:
    tmp_dest_dir_path: str = '../tmp_test_jupyter_util_3/'
    shutil.rmtree(tmp_dest_dir_path, ignore_errors=True)

    _: Stage = Stage()
    jupyter_util.display_on_colaboratory(
        html_file_name='test_file.html', dest_dir_path=tmp_dest_dir_path)
    expected_file_path: str = os.path.join(
        tmp_dest_dir_path, 'test_file.html')
    assert os.path.isfile(expected_file_path)

    shutil.rmtree(tmp_dest_dir_path, ignore_errors=True)
