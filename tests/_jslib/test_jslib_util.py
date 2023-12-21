import os
import shutil
from typing import List

from apysc._jslib import jslib_util
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings

_EXPECTED_JQUERY_FILE_NAME: str = "jquery-3.7.1.slim.min.js"
_EXPECTED_SVG_FILE_NAME: str = "svg-3.1.2.min.js"
_EXPECTED_JQUERY_MOUSEWHEEL_FILE_NAME: str = "jquery.mousewheel-3.1.13.min.js"


@apply_test_settings()
def test_get_jslib_file_names() -> None:
    jslib_file_names: List[str] = jslib_util.get_jslib_file_names()
    assert _EXPECTED_JQUERY_FILE_NAME in jslib_file_names
    assert _EXPECTED_SVG_FILE_NAME in jslib_file_names


@apply_test_settings()
def test_get_jslib_abs_dir_path() -> None:
    jslib_abs_dir_path: str = jslib_util.get_jslib_abs_dir_path()
    file_names: List[str] = os.listdir(jslib_abs_dir_path)
    assert _EXPECTED_JQUERY_FILE_NAME in file_names


@apply_test_settings()
def test_export_jslib_to_specified_dir() -> None:
    tmp_dir_path: str = "../.tmp_apysc_jslib_util_test/"
    shutil.rmtree(tmp_dir_path, ignore_errors=True)

    dest_file_path: str = jslib_util.export_jslib_to_specified_dir(
        dest_dir_path=tmp_dir_path, jslib_name=_EXPECTED_JQUERY_FILE_NAME
    )
    exported_dir_path: str = os.path.dirname(dest_file_path)
    assert tmp_dir_path == f"{exported_dir_path}/"
    assert dest_file_path.endswith(_EXPECTED_JQUERY_FILE_NAME)
    assert os.path.isfile(dest_file_path)

    testing_helper.assert_raises(
        expected_error_class=FileNotFoundError,
        callable_=jslib_util.export_jslib_to_specified_dir,
        dest_dir_path=tmp_dir_path,
        jslib_name="not_existing_lib.js",
    )

    shutil.rmtree(tmp_dir_path, ignore_errors=True)


@apply_test_settings()
def test_read_jslib_str() -> None:
    jslib_str: str = jslib_util.read_jslib_str(jslib_name=_EXPECTED_JQUERY_FILE_NAME)
    assert jslib_str != ""


@apply_test_settings()
def test__sort_js_file_names_with_priority_setting() -> None:
    sorted_jslib_file_names: List[
        str
    ] = jslib_util._sort_js_file_names_with_priority_setting(
        jslib_file_names=[
            _EXPECTED_SVG_FILE_NAME,
            _EXPECTED_JQUERY_MOUSEWHEEL_FILE_NAME,
            _EXPECTED_JQUERY_FILE_NAME,
        ]
    )
    assert sorted_jslib_file_names == [
        _EXPECTED_JQUERY_FILE_NAME,
        _EXPECTED_JQUERY_MOUSEWHEEL_FILE_NAME,
        _EXPECTED_SVG_FILE_NAME,
    ]


@apply_test_settings()
def test_get_jquery_file_name() -> None:
    file_name: str = jslib_util.get_jquery_file_name()
    assert file_name == _EXPECTED_JQUERY_FILE_NAME
