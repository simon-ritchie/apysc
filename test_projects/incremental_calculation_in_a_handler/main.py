"""Test project to check the behavior of the incremental calculation
in a handler.

Command examples:
$ python test_projects/incremental_calculation_in_a_handler/main.py
$ python incremental_calculation_in_a_handler/main.py
"""

import sys
from typing import Any, Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import Int, MouseEvent
from apysc import LineDotSetting
from apysc import Number
from apysc import Rectangle
from apysc import Sprite
from apysc import Stage
from apysc import String
from apysc import assert_not_equal
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
    sprite.graphics.begin_fill(color='#0af')
    rectangle: Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle.click(on_rectangle_click)

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_rectangle_click(
        e: MouseEvent[Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler called when a rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle = e.this
    rectangle.y += 50


if __name__ == '__main__':
    main()
