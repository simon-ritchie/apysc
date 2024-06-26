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
        background_color=ap.Color("#333"),
        stage_width=1200,
        stage_height=900,
    )

    circle_1: ap.Circle = ap.Circle(
        x=200,
        y=200,
        radius=50,
        fill_color=ap.Color("#0af"),
        line_color=ap.Color("#fff"),
        line_thickness=5,
    )
    bounding_box_rectangle_1: ap.Rectangle = ap.Rectangle(
        x=50,
        y=50,
        width=50,
        height=50,
        line_color=ap.Color("#fff"),
        line_thickness=1,
        line_alpha=0.3,
    )
    timer: ap.Timer = ap.Timer(
        handler=on_timer,
        delay=1000,
        options={
            "circle": circle_1,
            "bounding_box_rectangle": bounding_box_rectangle_1,
        },
    )
    timer.start()

    sprite_1: ap.Sprite = ap.Sprite()
    sprite_1.x = ap.Number(400)
    sprite_1.y = ap.Number(200)
    circle_2: ap.Circle = ap.Circle(
        x=0,
        y=0,
        radius=50,
        fill_color=ap.Color("#f0a"),
        parent=sprite_1,
    )
    bounding_box_1: ap.RectangleGeom = circle_2.get_bounds(
        target_coordinate_space_object=sprite_1
    )
    ap.Rectangle(
        x=bounding_box_1.left_x,
        y=bounding_box_1.top_y,
        width=bounding_box_1.width,
        height=bounding_box_1.height,
        line_color=ap.Color("#fff"),
        line_thickness=1,
        parent=sprite_1,
    )
    ap.assert_equal(bounding_box_1.left_x, -50)
    ap.assert_equal(bounding_box_1.top_y, -50)
    ap.assert_equal(bounding_box_1.right_x, 50)
    ap.assert_equal(bounding_box_1.bottom_y, 50)
    ap.assert_equal(bounding_box_1.width, 100)
    ap.assert_equal(bounding_box_1.height, 100)

    sprite_2: ap.Sprite = ap.Sprite()
    sprite_2.x = ap.Number(600)
    sprite_2.y = ap.Number(200)
    circle_3: ap.Circle = ap.Circle(
        x=50,
        y=50,
        radius=50,
        fill_color=ap.Color("#fa0"),
        parent=sprite_2,
    )
    bounding_box_2: ap.RectangleGeom = circle_3.get_bounds(
        target_coordinate_space_object=sprite_2
    )
    ap.Rectangle(
        x=bounding_box_2.left_x,
        y=bounding_box_2.top_y,
        width=bounding_box_2.width,
        height=bounding_box_2.height,
        line_color=ap.Color("#fff"),
        line_thickness=1,
        parent=sprite_2,
    )
    ap.assert_equal(bounding_box_2.left_x, 0)
    ap.assert_equal(bounding_box_2.top_y, 0)
    ap.assert_equal(bounding_box_2.right_x, 100)
    ap.assert_equal(bounding_box_2.bottom_y, 100)
    ap.assert_equal(bounding_box_2.width, 100)
    ap.assert_equal(bounding_box_2.height, 100)

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
