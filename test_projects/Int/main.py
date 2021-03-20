"""Test project for `Int` class.

Command examples:
$ python test_projects/Int/main.py
$ python Int/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apyscript.console.assertion import assert_equal
from apyscript.display import Stage
from apyscript.file import file_util
from apyscript.html import exporter
from apyscript.type import Int
from apyscript.type import Number

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

    int_1: Int = Int(10)
    assert_equal(expected=10, actual=int_1)

    int_2: Int = int_1 + 20
    assert_equal(expected=30, actual=int_2)

    int_3: Int = int_1 + int_2
    assert_equal(expected=40, actual=int_3)

    int_4: Int = Int(40) - 10
    assert_equal(expected=30, actual=int_4)

    int_5: Int = int_4 - int_1
    assert_equal(expected=20, actual=int_5)

    number_1: Number = int_1 / 4
    assert_equal(expected=2.5, actual=number_1)

    number_2: Number = int_1 / int_3
    assert_equal(expected=0.25, actual=number_2)

    int_6: Int = Int(30.5)
    assert_equal(expected=30, actual=int_6)

    int_7: Int = Int(Number(60.5))
    assert_equal(expected=60, actual=int_7)

    int_8: Int = Int(10) // 4
    assert_equal(expected=2, actual=int_8)

    int_9: Int = Int(10) // Int(3)
    assert_equal(expected=3, actual=int_9)

    int_10: Int = Int(10)
    int_10 += 5
    assert_equal(expected=15, actual=int_10)

    int_11: Int = Int(10)
    int_11 -= 3
    assert_equal(expected=7, actual=int_11)

    int_12: Int = Int(10)
    int_12 *= 3
    assert_equal(expected=30, actual=int_12)

    int_13: Int = Int(10)
    int_13 /= 4
    assert_equal(expected=2.5, actual=int_13)

    exporter.save_expressions_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
