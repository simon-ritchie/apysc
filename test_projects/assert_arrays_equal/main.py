"""Test project for `assert_arrays_equal` and `assert_arrays_not_equal`
interfaces.

Command examples:
$ python test_projects/assert_arrays_equal/main.py
$ python assert_arrays_equal/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc import Array
from apysc import Stage
from apysc import assert_arrays_equal
from apysc import assert_arrays_not_equal
from apysc import assert_equal
from apysc import assert_not_equal
from apysc.file import file_util
from apysc.html import exporter

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """
    Entry point of this test project.
    """
    _: Stage = Stage(background_color='#333')

    assert_arrays_equal(
        expected=[1, 2, 3], actual=[1, 2, 3])
    assert_arrays_equal(
        expected=(1, 2, 3), actual=[1, 2, 3])
    assert_arrays_equal(
        expected=[1, 2, 3], actual=(1, 2, 3))
    assert_arrays_equal(
        expected=(1, 2, 3), actual=(1, 2, 3))
    assert_arrays_equal(
        expected=Array([1, 2, 3]), actual=[1, 2, 3])
    assert_arrays_equal(
        expected=[1, 2, 3], actual=Array([1, 2, 3]))
    assert_arrays_equal(
        expected=Array([1, 2, 3]), actual=Array([1, 2, 3]))

    assert_arrays_not_equal(
        expected=[1, 2, 3], actual=[1, 2])
    assert_arrays_not_equal(
        expected=(1, 2, 3), actual=[1, 2])
    assert_arrays_not_equal(
        expected=[1, 2, 3], actual=Array([1, 2]))
    assert_arrays_not_equal(
        expected=Array([1, 2, 3]), actual=Array([1, 2]))

    assert_equal(
        expected=Array([1, 2, 3]), actual=Array([1, 2, 3]))
    assert_equal(
        expected=[1, 2, 3], actual=Array([1, 2, 3]))

    assert_not_equal(
        expected=Array([1, 2, 3]), actual=Array([1, 2]))
    assert_not_equal(
        expected=[1, 2, 3], actual=Array([1, 2]))

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
