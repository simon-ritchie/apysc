"""Test project for `Number` class.

Command examples:
$ python test_projects/Number/main.py
$ python Number/main.py
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

    number_1: ap.Number = ap.Number(value=10.5)
    ap.assert_equal(expected=10.5, actual=number_1)

    number_2: ap.Number = number_1 + 20.6
    ap.assert_equal(expected=31.1, actual=number_2)

    number_3: ap.Number = number_1 + number_2
    ap.assert_equal(expected=41.6, actual=number_3)

    number_4: ap.Number = ap.Number(value=30.5) - 10.2
    ap.assert_equal(expected=20.3, actual=number_4)

    number_5: ap.Number = number_4 - number_1
    ap.assert_equal(expected=9.8, actual=number_5)

    number_6: ap.Number = ap.Number(value=10) / 4
    ap.assert_equal(expected=2.5, actual=number_6)

    number_7: ap.Number = number_6 / ap.Number(value=10)
    ap.assert_equal(expected=0.25, actual=number_7)

    int_1: ap.Int = ap.Number(10.5) // 3
    ap.assert_equal(expected=3, actual=int_1)

    int_2: ap.Int = ap.Number(10.5) // ap.Number(3.1)
    ap.assert_equal(expected=3, actual=int_2)

    number_8: ap.Number = ap.Number(value=10.5)
    number_8 += 3.3
    ap.assert_equal(expected=13.8, actual=number_8)

    number_9: ap.Number = ap.Number(value=10.5)
    number_9 -= 3.2
    ap.assert_equal(expected=7.3, actual=number_9)

    number_10: ap.Number = ap.Number(value=10.5)
    number_10 *= 3
    ap.assert_equal(expected=31.5, actual=number_10)

    number_11: ap.Number = ap.Number(value=10.6)
    number_11 /= 2
    ap.assert_equal(expected=5.3, actual=number_11)

    number_12: ap.Number = ap.Number(value=10.5)
    number_13: ap.Number = number_12 % 3
    ap.assert_equal(expected=number_13, actual=1.5)
    number_14: ap.Number = number_12 % ap.Int(3)
    ap.assert_equal(expected=number_14, actual=1.5)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
