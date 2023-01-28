import os
import shutil
from random import randint

from retrying import retry

import apysc as ap
from apysc._jupyter import jupyter_util
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_display_on_jupyter() -> None:
    original_tmp_root_dir: str = jupyter_util._TMP_ROOT_DIR_PATH
    jupyter_util._TMP_ROOT_DIR_PATH = "../tmp_test_1/"

    ap.Stage()
    jupyter_util.display_on_jupyter(html_file_name="test_file.html")
    assert os.path.isfile("test_file.html")

    shutil.rmtree(jupyter_util._TMP_ROOT_DIR_PATH, ignore_errors=True)
    jupyter_util._TMP_ROOT_DIR_PATH = original_tmp_root_dir
    os.remove("test_file.html")


@apply_test_settings()
def test__save_overall_html() -> None:
    original_tmp_root_dir: str = jupyter_util._TMP_ROOT_DIR_PATH
    jupyter_util._TMP_ROOT_DIR_PATH = "../tmp_test_2/"
    _: ap.Stage = ap.Stage()
    jupyter_util._save_overall_html(html_file_name="test_file.html", minify=True)
    assert os.path.isfile("test_file.html")

    shutil.rmtree(jupyter_util._TMP_ROOT_DIR_PATH, ignore_errors=True)
    jupyter_util._TMP_ROOT_DIR_PATH = original_tmp_root_dir
    os.remove("test_file.html")


@apply_test_settings()
def test_display_on_colaboratory() -> None:
    original_tmp_root_dir: str = jupyter_util._TMP_ROOT_DIR_PATH
    jupyter_util._TMP_ROOT_DIR_PATH = "../tmp_test_3/"

    _: ap.Stage = ap.Stage()
    jupyter_util.display_on_colaboratory(html_file_name="test_file.html")
    assert os.path.isfile("test_file.html")

    shutil.rmtree(jupyter_util._TMP_ROOT_DIR_PATH, ignore_errors=True)
    jupyter_util._TMP_ROOT_DIR_PATH = original_tmp_root_dir
    os.remove("test_file.html")
