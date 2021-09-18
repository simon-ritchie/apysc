"""Test project for `Int` class.

Command examples:
$ python test_projects/Int/main.py
$ python Int/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from typing_extensions import TypedDict

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


class _Int15Options(TypedDict):
    int_15: ap.Int


def main() -> None:
    """
    Entry point of this test project.
    """
    stage: ap.Stage = ap.Stage(background_color='#333')

    int_1: ap.Int = ap.Int(10)
    ap.assert_equal(expected=10, actual=int_1)

    int_2: ap.Int = int_1 + 20
    ap.assert_equal(expected=30, actual=int_2)

    int_3: ap.Int = int_1 + int_2
    ap.assert_equal(expected=40, actual=int_3)

    int_4: ap.Int = ap.Int(40) - 10
    ap.assert_equal(expected=30, actual=int_4)

    int_5: ap.Int = int_4 - int_1
    ap.assert_equal(expected=20, actual=int_5)

    number_1: ap.Number = int_1 / 4
    ap.assert_equal(expected=2.5, actual=number_1)

    number_2: ap.Number = int_1 / int_3
    ap.assert_equal(expected=0.25, actual=number_2)

    int_6: ap.Int = ap.Int(30.5)
    ap.assert_equal(expected=30, actual=int_6)

    int_7: ap.Int = ap.Int(ap.Number(60.5))
    ap.assert_equal(expected=60, actual=int_7)

    int_8: ap.Int = ap.Int(10) // 4
    ap.assert_equal(expected=2, actual=int_8)

    int_9: ap.Int = ap.Int(10) // ap.Int(3)
    ap.assert_equal(expected=3, actual=int_9)

    int_10: ap.Int = ap.Int(10)
    int_10 += 5
    ap.assert_equal(expected=15, actual=int_10)

    int_11: ap.Int = ap.Int(10)
    int_11 -= 3
    ap.assert_equal(expected=7, actual=int_11)

    int_12: ap.Int = ap.Int(10)
    int_12 *= 3
    ap.assert_equal(expected=30, actual=int_12)

    int_13: ap.Int = ap.Int(10)
    int_13 /= 4
    ap.assert_equal(expected=2.5, actual=int_13)

    int_14: ap.Int = ap.Int(10)
    boolean_1: ap.Boolean = ap.Boolean(False)
    with ap.If(boolean_1, locals(), globals()):
        int_14 += 10
    ap.assert_equal(expected=10, actual=int_14)

    with ap.If(boolean_1, locals(), globals()):
        int_14 -= 10
    ap.assert_equal(expected=10, actual=int_14)

    with ap.If(boolean_1, locals(), globals()):
        int_14 *= 2
    ap.assert_equal(expected=10, actual=int_14)

    with ap.If(boolean_1, locals(), globals()):
        int_14 /= 2
    ap.assert_equal(expected=10, actual=int_14)

    int_15: ap.Int = ap.Int(10)
    options: _Int15Options = {'int_15': int_15}
    stage.click(on_stage_clicked, options=options)

    int_16: ap.Int = ap.Int(10)
    int_17: ap.Int = int_16 % 3
    ap.assert_equal(expected=1, actual=int_17)
    int_18: ap.Int = int_16 % ap.Int(3)
    ap.assert_equal(expected=1, actual=int_18)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_stage_clicked(e: ap.MouseEvent, options: _Int15Options) -> None:
    """
    Test handler that called when stage is clicked.

    Parameters
    ----------
    e : MouseEvent
        Created event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('stage clicked!')
    int_15: ap.Int = options['int_15']
    int_15 += 5
    ap.assert_true(int_15 == 15)
    ap.assert_true(int_15 != 16)
    ap.assert_true(int_15 < 16)
    ap.assert_true(int_15 <= 15)
    ap.assert_true(int_15 > 14)
    ap.assert_true(int_15 >= 15)


if __name__ == '__main__':
    main()
