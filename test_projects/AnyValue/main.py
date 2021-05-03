"""Test project for `AnyValue` class.

Command examples:
$ python test_projects/AnyValue/main.py
$ python AnyValue/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc import AnyValue, Boolean
from apysc import Int
from apysc import Stage
from apysc import assert_equal, assert_true, assert_false
from apysc.file import file_util
from apysc.html import exporter

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """Entry point of this test project.
    """
    _: Stage = Stage(background_color='#333')

    any_value_1: AnyValue = AnyValue(10)
    any_value_1 = any_value_1 + 10
    assert_equal(expected=20, actual=any_value_1)

    any_value_2: AnyValue = AnyValue(20)
    int_1: Int = Int(10)
    any_value_2 = any_value_2 - int_1
    assert_equal(expected=10, actual=any_value_2)

    any_value_3: AnyValue = AnyValue(10)
    any_value_3 = any_value_3 * 3
    assert_equal(expected=30, actual=any_value_3)

    any_value_4: AnyValue = AnyValue(50)
    any_value_4 = any_value_4 / 2
    assert_equal(expected=25, actual=any_value_4)

    any_value_5: AnyValue = AnyValue(10)
    any_value_5 = any_value_5 // 3
    assert_equal(expected=3, actual=any_value_5)

    any_value_6: AnyValue = AnyValue(20)
    any_value_6 += 30
    assert_equal(expected=50, actual=any_value_6)

    any_value_7: AnyValue = AnyValue(60)
    any_value_7 -= 25
    assert_equal(expected=35, actual=(any_value_7))

    any_value_8: AnyValue = AnyValue(3)
    any_value_8 *= 10
    assert_equal(expected=30, actual=any_value_8)

    any_value_9: AnyValue = AnyValue(20)
    any_value_9 /= 4
    assert_equal(expected=5, actual=any_value_9)

    any_value_10: AnyValue = AnyValue(10)
    result: Boolean = any_value_10 == 10
    assert_true(result)
    result = any_value_10 == 11
    assert_false(result)

    result = any_value_10 != 11
    assert_true(result)
    result = any_value_10 != 10
    assert_false(result)

    result = any_value_10 < 11
    assert_true(result)
    result = any_value_10 < 10
    assert_false(result)

    result = any_value_10 <= 10
    assert_true(result)
    result = any_value_10 <= 9
    assert_false(result)

    result = any_value_10 > 9
    assert_true(result)
    result = any_value_10 > 10
    assert_false(result)

    result = any_value_10 >= 10
    assert_true(result)
    result = any_value_10 >= 11
    assert_false(result)

    exporter.save_expressions_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
