"""Test project for `Point2D` class.

Command examples:
$ python test_projects/Point2D/main.py
$ python Point2D/main.py
"""

import sys
from typing import Any
from typing import Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import Array, Point2D
from apysc import If
from apysc import Int
from apysc import MouseEvent
from apysc import Stage
from apysc import String
from apysc import assert_arrays_equal
from apysc import assert_equal
from apysc import assert_true
from apysc import trace
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
    stage: Stage = Stage(background_color='#333')

    point: Point2D = Point2D(x=10, y=20)
    assert_equal(expected=10, actual=point.x)
    assert_equal(expected=20, actual=point.y)

    x: Int = Int(30)
    y: Int = Int(40)
    point = Point2D(x=x, y=y)
    assert_equal(expected=30, actual=point.x)
    assert_equal(expected=40, actual=point.y)

    point.x = 50
    point.y = 60
    assert_equal(expected=50, actual=point.x)
    assert_equal(expected=60, actual=point.y)

    x.value = 70
    y.value = 80
    point.x = x
    point.y = y
    assert_equal(expected=70, actual=point.x)
    assert_equal(expected=80, actual=point.y)

    exporter.save_expressions_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
