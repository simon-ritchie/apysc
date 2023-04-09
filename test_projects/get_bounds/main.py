"""The test project for the `get_bounds` method interface.

Command examples:
$ python test_projects/get_bounds/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

from typing_extensions import TypedDict

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


class _TimerOptions(TypedDict):
    circle: ap.Circle
    bounding_box_rectangle: ap.Rectangle


def main() -> None:
    """
    Entry point of this test project.
    """
    _: ap.Stage = ap.Stage(
        background_color="#333",
        stage_width=1200,
        stage_height=900,
    )

    circle: ap.Circle = ap.Circle(
        x=200,
        y=200,
        radius=50,
        fill_color="#0af",
        line_color="#fff",
        line_thickness=5,
    )
    bounding_box_rectangle: ap.Rectangle = ap.Rectangle(
        x=50,
        y=50,
        width=50,
        height=50,
        line_color="#fff",
        line_thickness=1,
        line_alpha=0.3,
    )
    timer: ap.Timer = ap.Timer(
        handler=on_timer,
        delay=1000,
        options={
            "circle": circle,
            "bounding_box_rectangle": bounding_box_rectangle,
        },
    )
    timer.start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_timer(e: ap.TimerEvent, options: _TimerOptions) -> None:
    """
    The handler to handle a timer event.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : _TimerOptions
        Optional argument dictionary.
    """
    timer: ap.Timer = e.this
    circle: ap.Circle = options["circle"]
    bounding_box_rectangle = options["bounding_box_rectangle"]

    with ap.If(timer.current_count == 2):
        circle.scale_x_from_center = ap.Number(0.7)
    with ap.If(timer.current_count == 3):
        circle.scale_y_from_center = ap.Number(0.4)
    with ap.If(timer.current_count == 4):
        circle.rotation_around_center = ap.Int(30)
    with ap.If(timer.current_count == 5):
        circle.rotation_around_center = ap.Int(90)
    bounding_box: ap.RectangleGeom = circle.get_bounds()
    bounding_box_rectangle.x = bounding_box.left_x
    bounding_box_rectangle.y = bounding_box.top_y
    bounding_box_rectangle.width = bounding_box.width
    bounding_box_rectangle.height = bounding_box.height


if __name__ == "__main__":
    main()
