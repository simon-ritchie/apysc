import os
import shutil
from random import randint
from typing import Any
from typing import Dict
from typing import List

from retrying import retry

from apysc._jslib import jslib_util
from apysc._testing import testing_helper


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_jslib_file_names() -> None:
    jslib_file_names: List[str] = jslib_util.get_jslib_file_names()
    assert 'jquery.min.js' in jslib_file_names
    assert 'svg.min.js' in jslib_file_names


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_jslib_abs_dir_path() -> None:
    jslib_abs_dir_path: str = jslib_util.get_jslib_abs_dir_path()
    file_names: List[str] = os.listdir(jslib_abs_dir_path)
    assert 'jquery.min.js' in file_names


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_export_jslib_to_specified_dir() -> None:
    tmp_dir_path: str = '../.tmp_apysc_jslib_util_test/'
    shutil.rmtree(tmp_dir_path, ignore_errors=True)

    dest_file_path: str = jslib_util.export_jslib_to_specified_dir(
        dest_dir_path=tmp_dir_path,
        jslib_name='jquery.min.js')
    exported_dir_path: str = os.path.dirname(dest_file_path)
    assert tmp_dir_path == f'{exported_dir_path}/'
    assert dest_file_path.endswith('jquery.min.js')
    assert os.path.isfile(dest_file_path)

    kwargs: Dict[str, Any] = {
        'dest_dir_path': tmp_dir_path,
        'jslib_name': 'not_existing_lib.js',
    }
    testing_helper.assert_raises(
        expected_error_class=FileNotFoundError,
        callable_=jslib_util.export_jslib_to_specified_dir,
        kwargs=kwargs)

    shutil.rmtree(tmp_dir_path, ignore_errors=True)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_read_jslib_str() -> None:
    jslib_str: str = 'jquery.min.js'
    assert jslib_str != ''


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__sort_js_file_names_with_priority_setting() -> None:
    sorted_jslib_file_names: List[str] = jslib_util.\
        _sort_js_file_names_with_priority_setting(
            jslib_file_names=[
                'svg.min.js',
                'jquery.mousewheel.min.js',
                'jquery.min.js',
            ])
    assert sorted_jslib_file_names == [
        'jquery.min.js',
        'jquery.mousewheel.min.js',
        'svg.min.js',
    ]
