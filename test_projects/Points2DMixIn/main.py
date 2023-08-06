"""Test project for `Points2DMixIn` class.

Command examples:
$ python test_projects/Points2DMixIn/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

import apysc as ap
from apysc._display.points_2d_mixin import Points2DMixIn
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


def main() -> None:
    """Entry point of this test project."""
    _: ap.Stage = ap.Stage(background_color=ap.Color("#333"))

    interface: Points2DMixIn = Points2DMixIn()
    interface.variable_name = "test_point_2d_interface"

    interface.points = ap.Array([ap.Point2D(10, 20), ap.Point2D(30, 40)])
    ap.assert_equal(left=ap.Point2D(10, 20), right=interface.points[0])
    interface.points[1] = ap.Point2D(50, 60)
    ap.assert_equal(left=ap.Point2D(50, 60), right=interface.points[1])

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == "__main__":
    main()
