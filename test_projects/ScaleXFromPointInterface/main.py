"""The test project for the ScaleXFromPointInterface class.

Command examples:
$ python test_projects/ScaleXFromPointInterface/main.py
$ python ScaleXFromPointInterface/main.py
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


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def main() -> None:
    """
    Entry point of this test project.
    """
    stage: ap.Stage = ap.Stage(
        background_color='#333',
        stage_width=1000, stage_height=500, stage_elem_id='stage')
    sprite: ap.Sprite = ap.Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#0af')
    rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    options: _RectOptions = {'rectangle': rectangle_1}
    timer_1: ap.Timer = ap.Timer(
        on_timer_1, delay=ap.FPS.FPS_60, options=options)
    timer_1.start()

    rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
        x=100, y=150, width=50, height=50)
    rectangle_2.set_scale_x_from_point(scale_x=ap.Number(2.0), x=ap.Int(150))

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_timer_1(e: ap.TimerEvent, options: _RectOptions) -> None:
    """
    The handler will be called from a timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options['rectangle']
    x: ap.Int = ap.Int(50)
    scale_x: ap.Number = rectangle.get_scale_x_from_point(x=x)
    scale_x += 0.03
    rectangle.set_scale_x_from_point(scale_x=scale_x, x=x)

    with ap.If(scale_x >= 5.0):
        rectangle.set_scale_x_from_point(scale_x=ap.Number(5.0), x=x)
        e.this.stop()


if __name__ == '__main__':
    main()
