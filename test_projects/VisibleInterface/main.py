"""Test project for VisibleInterface class.

Command examples:
$ python test_projects/VisibleInterface/main.py
$ python VisibleInterface/main.py
"""

import sys
from typing import Any, Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import Boolean, Rectangle, MouseEvent
from apysc import Int
from apysc import Sprite
from apysc import Stage
from apysc import assert_defined
from apysc import assert_equal
from apysc import assert_false
from apysc import assert_true
from apysc import assert_undefined
from apysc.display.display_object import DisplayObject
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
    stage: Stage = Stage(background_color='#333', stage_height=300)

    sprite_1: Sprite = Sprite(stage=stage)
    sprite_1.graphics.begin_fill(color='#0af')
    rectangle_1: Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle_2: Rectangle = sprite_1.graphics.draw_rect(
        x=150, y=50, width=50, height=50)
    rectangle_2.visible = Boolean(False)

    sprite_2: Sprite = Sprite(stage=stage)
    sprite_2.graphics.begin_fill(color='#f0a')
    rectangle_3: Rectangle = sprite_2.graphics.draw_rect(
        x=50, y=150, width=50, height=50)
    rectangle_4: Rectangle = sprite_2.graphics.draw_rect(
        x=150, y=150, width=50, height=50)
    sprite_2.visible = Boolean(False)

    rectangle_1.click(
        on_rectangle_1_click,
        options={
            'sprite_2': sprite_2,
            'rectangle_3': rectangle_3,
            'rectangle_4': rectangle_4})
    rectangle_3.click(on_rectangle_3_or_4_click)
    rectangle_4.click(on_rectangle_3_or_4_click)

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


def on_rectangle_1_click(e: MouseEvent, options: Dict[str, Any]) -> None:
    """
    Handler that called when rectangle_1 is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional values.
    """
    sprite_2: Sprite = options['sprite_2']
    sprite_2.visible = Boolean(True)
    rectangle_3: Rectangle = options['rectangle_3']
    rectangle_3.visible = Boolean(True)
    rectangle_4: Rectangle = options['rectangle_4']
    rectangle_4.visible = Boolean(True)


def on_rectangle_3_or_4_click(
        e: MouseEvent[Rectangle], options: Dict[str, Any]) -> None:
    """
    Handler that called when rectangle_3 or rectangle_4 is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional values.
    """
    e.this.visible = Boolean(False)


if __name__ == '__main__':
    main()

