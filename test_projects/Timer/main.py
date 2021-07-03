"""The test project for the Timer class.

Command examples:
$ python test_projects/Timer/main.py
$ python Timer/main.py
"""

import sys
from typing import Any, Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import Timer, Stage, Sprite, Rectangle, TimerEvent, MouseEvent
from apysc import save_overall_html
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
    stage: Stage = Stage(
        background_color='#333',
        stage_width=1000, stage_height=500)
    sprite: Sprite = Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#0af')
    rectangle_1: Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    timer: Timer = Timer(
        handler=on_timer_1, delay=16.6,
        options={'rect': rectangle_1})
    timer.start()

    sprite.graphics.begin_fill(color='#f0a')
    rectangle_2: Rectangle = sprite.graphics.draw_rect(
        x=150, y=50, width=50, height=50)
    rectangle_2.click(on_rectangle_click)

    save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_timer_1(e: TimerEvent, options: Dict[str, Any]) -> None:
    """
    The handler would be called from a timer instance.

    Parameters
    ----------
    e : TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rect: Rectangle = options['rect']
    rect.y += 1


def on_rectangle_click(
        e: MouseEvent[Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler would be called when a rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    timer: Timer = Timer(
        handler=on_timer_1,
        delay=33.3,
        options={'rect': e.this})
    timer.start()


if __name__ == '__main__':
    main()
