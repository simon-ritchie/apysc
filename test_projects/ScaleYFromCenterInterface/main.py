"""The test project for the ScaleYFromCenterInterface class.

Command examples:
$ python test_projects/ScaleYFromCenterInterface/main.py
$ python ScaleYFromCenterInterface/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType
from typing import Any
from typing import Dict

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
    rectangle_1.scale_y_from_center = ap.Number(0.5)

    rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
        x=150, y=50, width=50, height=50)
    rectangle_2.scale_y_from_center = ap.Number(0.5)
    rectangle_2.scale_y_from_center = ap.Number(1)

    rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
        x=250, y=50, width=50, height=50)
    options: _RectOptions = {'rectangle': rectangle_3}
    timer_1: ap.Timer = ap.Timer(
        on_timer_1, delay=ap.FPS.FPS_60,
        options=options)
    timer_1.start()

    rectangle_4: ap.Rectangle = sprite.graphics.draw_rect(
        x=350, y=50, width=50, height=50)
    options = {'rectangle': rectangle_4}
    timer_2: ap.Timer = ap.Timer(
        on_timer_2, delay=ap.FPS.FPS_60,
        options=options)
    timer_2.start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


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
    scale_y_from_center: ap.Number = rectangle.scale_y_from_center
    rectangle.scale_y_from_center = scale_y_from_center - 0.01


def on_timer_2(e: ap.TimerEvent, options: _RectOptions) -> None:
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
    rectangle.scale_y_from_center -= 0.01


if __name__ == '__main__':
    main()
