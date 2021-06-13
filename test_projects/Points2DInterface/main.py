"""Test project for `Points2DInterface` class.

Command examples:
$ python test_projects/Points2DInterface/main.py
$ python Points2DInterface/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc import Array
from apysc import Point2D
from apysc import Stage
from apysc import assert_equal
from apysc import save_overall_html
from apysc.display.points_2d_interface import Points2DInterface
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

    interface: Points2DInterface = Points2DInterface()
    interface.variable_name = 'test_point_2d_interface'

    interface.points = Array([Point2D(10, 20), Point2D(30, 40)])
    assert_equal(expected=Point2D(10, 20), actual=interface.points[0])
    interface.points[1] = Point2D(50, 60)
    assert_equal(expected=Point2D(50, 60), actual=interface.points[1])

    save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
