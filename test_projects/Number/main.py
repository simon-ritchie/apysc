"""Test project for `Number` class.

Command examples:
$ python test_projects/Number/main.py
$ python Number/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc import Int
from apysc import Number
from apysc import Stage
from apysc import assert_equal
from apysc import save_overall_html
from apysc.file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """Entry point of this test project.
    """
    _: Stage = Stage(background_color='#333')

    number_1: Number = Number(value=10.5)
    assert_equal(expected=10.5, actual=number_1)

    number_2: Number = number_1 + 20.6
    assert_equal(expected=31.1, actual=number_2)

    number_3: Number = number_1 + number_2
    assert_equal(expected=41.6, actual=number_3)

    number_4: Number = Number(value=30.5) - 10.2
    assert_equal(expected=20.3, actual=number_4)

    number_5: Number = number_4 - number_1
    assert_equal(expected=9.8, actual=number_5)

    number_6: Number = Number(value=10) / 4
    assert_equal(expected=2.5, actual=number_6)

    number_7: Number = number_6 / Number(value=10)
    assert_equal(expected=0.25, actual=number_7)

    int_1: Int = Number(10.5) // 3
    assert_equal(expected=3, actual=int_1)

    int_2: Int = Number(10.5) // Number(3.1)
    assert_equal(expected=3, actual=int_2)

    number_8: Number = Number(value=10.5)
    number_8 += 3.3
    assert_equal(expected=13.8, actual=number_8)

    number_9: Number = Number(value=10.5)
    number_9 -= 3.2
    assert_equal(expected=7.3, actual=number_9)

    number_10: Number = Number(value=10.5)
    number_10 *= 3
    assert_equal(expected=31.5, actual=number_10)

    number_11: Number = Number(value=10.6)
    number_11 /= 2
    assert_equal(expected=5.3, actual=number_11)

    save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
