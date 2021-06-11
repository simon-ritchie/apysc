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

from apysc import Circle
from apysc import LineDotSetting
from apysc import MouseEvent
from apysc import Sprite
from apysc import Stage
from apysc.file import file_util
from apysc.html import exporter

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

    sprite.graphics.begin_fill(color='0af')
    circle: Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)
    circle.click(on_circle_click)

    sprite.graphics.begin_fill(color='')
    sprite.graphics.line_style(
        color='#fff', thickness=3,
        dot_setting=LineDotSetting(dot_size=3))
    circle = sprite.graphics.draw_circle(x=250, y=100, radius=100)

    exporter.save_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


def on_circle_click(e: MouseEvent[Circle], options: Dict[str, Any]) -> None:
    """
    The handler called when the circle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.x += 50
    e.this.y += 25


if __name__ == '__main__':
    main()
