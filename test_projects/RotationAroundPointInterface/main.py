"""The test project for the RotationAroundPointInterface class.

Command examples:
$ python test_projects/RotationAroundPointInterface/main.py
$ python RotationAroundPointInterface/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType
from typing import Any
from typing import Dict

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """
    Entry point of this test project.
    """
    stage: ap.Stage = ap.Stage(
        background_color='#333',
        stage_width=1000, stage_height=500)

    sprite_1: ap.Sprite = ap.Sprite(stage=stage)
    sprite_1.graphics.begin_fill(color='#0af', alpha=0.5)
    rectangle_1: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50)

    rectangle_2: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50)

    timer_1: ap.Timer = ap.Timer(
        handler=on_timer_1, delay=ap.FPS.FPS_60,
        options={'rectangle_1': rectangle_1, 'rectangle_2': rectangle_2})
    timer_1.start()

    sprite_2: ap.Sprite = ap.Sprite(stage=stage)
    sprite_2.graphics.begin_fill(color='#f0a', alpha=0.5)
    sprite_2.x = ap.Int(50)
    sprite_2.y = ap.Int(50)
    rectangle_3: ap.Rectangle = sprite_2.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    timer_2: ap.Timer = ap.Timer(
        handler=on_timer_2, delay=ap.FPS.FPS_60,
        options={'rectangle_3': rectangle_3})
    timer_2.start()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_timer_1(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler would be called from the first timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_1: ap.Rectangle = options['rectangle_1']
    rectangle_1.rotate_around_point(additional_rotation=1, x=50, y=50)

    rectangle_2: ap.Rectangle = options['rectangle_2']
    rectangle_2.rotate_around_point(additional_rotation=1, x=100, y=100)


def on_timer_2(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler would be called from the second timer.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_3: ap.Rectangle = options['rectangle_3']
    rectangle_3.rotate_around_point(additional_rotation=1, x=50, y=50)


if __name__ == '__main__':
    main()
