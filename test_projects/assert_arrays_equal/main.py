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

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """
    Entry point of this test project.
    """
    _: ap.Stage = ap.Stage(background_color='#333')

    ap.assert_arrays_equal(
        expected=[1, 2, 3], actual=[1, 2, 3])
    ap.assert_arrays_equal(
        expected=(1, 2, 3), actual=[1, 2, 3])
    ap.assert_arrays_equal(
        expected=[1, 2, 3], actual=(1, 2, 3))
    ap.assert_arrays_equal(
        expected=(1, 2, 3), actual=(1, 2, 3))
    ap.assert_arrays_equal(
        expected=ap.Array([1, 2, 3]), actual=[1, 2, 3])
    ap.assert_arrays_equal(
        expected=[1, 2, 3], actual=ap.Array([1, 2, 3]))
    ap.assert_arrays_equal(
        expected=ap.Array([1, 2, 3]), actual=ap.Array([1, 2, 3]))

    ap.assert_arrays_not_equal(
        expected=[1, 2, 3], actual=[1, 2])
    ap.assert_arrays_not_equal(
        expected=(1, 2, 3), actual=[1, 2])
    ap.assert_arrays_not_equal(
        expected=[1, 2, 3], actual=ap.Array([1, 2]))
    ap.assert_arrays_not_equal(
        expected=ap.Array([1, 2, 3]), actual=ap.Array([1, 2]))

    ap.assert_equal(
        expected=ap.Array([1, 2, 3]), actual=ap.Array([1, 2, 3]))
    ap.assert_equal(
        expected=[1, 2, 3], actual=ap.Array([1, 2, 3]))

    ap.assert_not_equal(
        expected=ap.Array([1, 2, 3]), actual=ap.Array([1, 2]))
    ap.assert_not_equal(
        expected=[1, 2, 3], actual=ap.Array([1, 2]))

    ap.save_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
