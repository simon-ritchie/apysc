"""Test project for `AnyValue` class.

Command examples:
$ python test_projects/AnyValue/main.py
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
    """Entry point of this test project.
    """
    _: ap.Stage = ap.Stage(background_color='#333')

    any_value_1: ap.AnyValue = ap.AnyValue(10)
    any_value_1 = any_value_1 + 10
    ap.assert_equal(expected=20, actual=any_value_1)

    any_value_2: ap.AnyValue = ap.AnyValue(20)
    int_1: ap.Int = ap.Int(10)
    any_value_2 = any_value_2 - int_1
    ap.assert_equal(expected=10, actual=any_value_2)

    any_value_3: ap.AnyValue = ap.AnyValue(10)
    any_value_3 = any_value_3 * 3
    ap.assert_equal(expected=30, actual=any_value_3)

    any_value_4: ap.AnyValue = ap.AnyValue(50)
    any_value_4 = any_value_4 / 2
    ap.assert_equal(expected=25, actual=any_value_4)

    any_value_5: ap.AnyValue = ap.AnyValue(10)
    any_value_5 = any_value_5 // 3
    ap.assert_equal(expected=3, actual=any_value_5)

    any_value_6: ap.AnyValue = ap.AnyValue(20)
    any_value_6 += 30
    ap.assert_equal(expected=50, actual=any_value_6)

    any_value_7: ap.AnyValue = ap.AnyValue(60)
    any_value_7 -= 25
    ap.assert_equal(expected=35, actual=(any_value_7))

    any_value_8: ap.AnyValue = ap.AnyValue(3)
    any_value_8 *= 10
    ap.assert_equal(expected=30, actual=any_value_8)

    any_value_9: ap.AnyValue = ap.AnyValue(20)
    any_value_9 /= 4
    ap.assert_equal(expected=5, actual=any_value_9)

    any_value_10: ap.AnyValue = ap.AnyValue(10)
    result: ap.Boolean = any_value_10 == 10
    ap.assert_true(result)
    result = any_value_10 == 11
    ap.assert_false(result)

    result = any_value_10 != 11
    ap.assert_true(result)
    result = any_value_10 != 10
    ap.assert_false(result)

    result = any_value_10 < 11
    ap.assert_true(result)
    result = any_value_10 < 10
    ap.assert_false(result)

    result = any_value_10 <= 10
    ap.assert_true(result)
    result = any_value_10 <= 9
    ap.assert_false(result)

    result = any_value_10 > 9
    ap.assert_true(result)
    result = any_value_10 > 10
    ap.assert_false(result)

    result = any_value_10 >= 10
    ap.assert_true(result)
    result = any_value_10 >= 11
    ap.assert_false(result)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
