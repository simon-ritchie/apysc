"""Test project for the draw_circle interface.

Command examples:
$ python test_projects/draw_circle/main.py
$ python draw_circle/main.py
"""

import sys
from typing import Any
from typing import Dict

sys.path.append('./')

import os
from types import ModuleType

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
    sprite: ap.Sprite = ap.Sprite(stage=stage)

    sprite.graphics.begin_fill(color='0af')
    circle_1: ap.Circle = sprite.graphics.draw_circle(
        x=100, y=100, radius=100)
    circle_1.click(on_circle_1_click)

    sprite.graphics.begin_fill(color='')
    sprite.graphics.line_style(
        color='#fff', thickness=3,
        dot_setting=ap.LineDotSetting(dot_size=3))
    circle_2 = sprite.graphics.draw_circle(x=250, y=100, radius=100)
    circle_2.click(on_circle_2_click)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_circle_1_click(
        e: ap.MouseEvent[ap.Circle], options: Dict[str, Any]) -> None:
    """
    The handler would be called when the circle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.x += 50
    e.this.y += 25


def on_circle_2_click(
        e: ap.MouseEvent[ap.Circle], options: Dict[str, Any]) -> None:
    """
    The handler would be called when the circle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.radius = ap.Int(110)


if __name__ == '__main__':
    main()
