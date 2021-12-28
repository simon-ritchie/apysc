"""Test project for `Point2D` class.

Command examples:
$ python test_projects/Point2D/main.py
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

    point: ap.Point2D = ap.Point2D(x=10, y=20)
    ap.assert_equal(left=10, right=point.x)
    ap.assert_equal(left=20, right=point.y)

    x: ap.Int = ap.Int(30)
    y: ap.Int = ap.Int(40)
    point = ap.Point2D(x=x, y=y)
    ap.assert_equal(left=30, right=point.x)
    ap.assert_equal(left=40, right=point.y)

    point.x = 50  # type: ignore
    point.y = 60  # type: ignore
    ap.assert_equal(left=50, right=point.x)
    ap.assert_equal(left=60, right=point.y)

    x.value = 70
    y.value = 80
    point.x = x
    point.y = y
    ap.assert_equal(left=70, right=point.x)
    ap.assert_equal(left=80, right=point.y)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
