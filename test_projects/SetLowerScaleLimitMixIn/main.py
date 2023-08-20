"""The test project for the SetLowerScaleLimitMixIn class.

Command examples:
$ python test_projects/SetLowerScaleLimitMixIn/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

from typing_extensions import TypedDict

import apysc as ap
from apysc._display.set_lower_scale_limit_mixin import MIN_SCALE
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


class _CircleOptions(TypedDict):
    circle_1: ap.Circle
    circle_2: ap.Circle
    circle_3: ap.Circle
    circle_4: ap.Circle


def main() -> None:
    """
    Entry point of this test project.
    """
    ap.Stage(
        background_color=ap.Color("#333"),
        stage_width=1000,
        stage_height=500,
        stage_elem_id="stage",
    )

    circle_1: ap.Circle = ap.Circle(
        x=100, y=100, radius=50, fill_color=ap.Color("#0af")
    )
    circle_2: ap.Circle = ap.Circle(
        x=200, y=100, radius=50, fill_color=ap.Color("#0af")
    )
    circle_3: ap.Circle = ap.Circle(
        x=300, y=100, radius=50, fill_color=ap.Color("#0af")
    )
    circle_4: ap.Circle = ap.Circle(
        x=400, y=100, radius=50, fill_color=ap.Color("#0af")
    )

    options: _CircleOptions = {
        "circle_1": circle_1,
        "circle_2": circle_2,
        "circle_3": circle_3,
        "circle_4": circle_4,
    }
    ap.Timer(on_timer, delay=1000, options=options).start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_timer(e: ap.TimerEvent, options: _CircleOptions) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : _CircleOptions
        Optional arguments dictionary.
    """
    circle_1: ap.Circle = options["circle_1"]
    with ap.If(circle_1.scale_x_from_center <= MIN_SCALE):
        circle_1.scale_x_from_center = ap.Number(1.0)
    with ap.Else():
        circle_1.scale_x_from_center = ap.Number(-0.5)
        ap.assert_equal(circle_1.scale_x_from_center, MIN_SCALE)

    circle_2: ap.Circle = options["circle_2"]
    with ap.If(circle_2.scale_y_from_center <= MIN_SCALE):
        circle_2.scale_y_from_center = ap.Number(1.0)
    with ap.Else():
        circle_2.scale_y_from_center = ap.Number(-0.5)
        ap.assert_equal(circle_2.scale_y_from_center, MIN_SCALE)

    circle_3: ap.Circle = options["circle_3"]
    with ap.If(circle_3.get_scale_x_from_point(x=ap.Number(300)) <= MIN_SCALE):
        circle_3.set_scale_x_from_point(scale_x=ap.Number(1.0), x=ap.Number(300))
    with ap.Else():
        circle_3.set_scale_x_from_point(scale_x=ap.Number(-0.5), x=ap.Number(300))
        ap.assert_equal(circle_3.get_scale_x_from_point(x=ap.Number(300)), MIN_SCALE)

    circle_4: ap.Circle = options["circle_4"]
    with ap.If(circle_4.get_scale_y_from_point(y=ap.Number(100)) <= MIN_SCALE):
        circle_4.set_scale_y_from_point(scale_y=ap.Number(1.0), y=ap.Number(100))
    with ap.Else():
        circle_4.set_scale_y_from_point(scale_y=ap.Number(-0.5), y=ap.Number(100))
        ap.assert_equal(circle_4.get_scale_y_from_point(y=ap.Number(100)), MIN_SCALE)


if __name__ == "__main__":
    main()
