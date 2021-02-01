from typing import List
from apyscript.jslib import jslib_util


def test_get_jslib_file_names() -> None:
    jslib_file_names: List[str] = jslib_util.get_jslib_file_names()
    assert 'jquery.min.js' in jslib_file_names
    assert 'svg.min.js' in jslib_file_names
