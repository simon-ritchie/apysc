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

from apyscript.console.assertion import assert_arrays_equal
from apyscript.display.stage import Stage
from apyscript.file import file_util
from apyscript.html import exporter
from apyscript.type import Array

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

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
