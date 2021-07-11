"""Test project to check the behavior of the incremental calculation
in a handler.

Command examples:
$ python test_projects/incremental_calculation_in_a_handler/main.py
$ python incremental_calculation_in_a_handler/main.py
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
    sprite_1: ap.Sprite = ap.Sprite(stage=stage)
    sprite_1.graphics.begin_fill(color='#0af')

    # The test pattern for the inscremental addition interface.
    rectangle_1: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle_1.click(on_rectangle_1_click)

    # The test pattern for the incremental subtraction interface.
    rectangle_2: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=150, y=400, width=50, height=50)
    rectangle_2.click(on_rectangle_2_click)

    # The test pattern for the incremental multiplication interface.
    rectangle_3: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=250, y=50, width=50, height=50)
    rectangle_3.click(on_rectangle_3_click)

    # The test pattern for the incremental true division interface.
    rectangle_4: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=350, y=400, width=50, height=50)
    rectangle_4.click(on_rectangle_4_click)

    # The test pattern for the container interface.
    sprite_2: ap.Sprite = ap.Sprite(stage=stage)
    sprite_2.graphics.begin_fill(color='#f0a')
    sprite_2.graphics.draw_rect(x=450, y=50, width=50, height=50)
    sprite_2.click(on_sprite_2_click)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_rectangle_1_click(
        e: ap.MouseEvent[ap.Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler called when a rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.y += 50


def on_rectangle_2_click(
        e: ap.MouseEvent[ap.Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler called when a rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.y -= 50


def on_rectangle_3_click(
        e: ap.MouseEvent, options: Dict[str, Any]) -> None:
    """
    The handler called when a rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.y *= 2


def on_rectangle_4_click(
        e: ap.MouseEvent[ap.Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler called when a rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.y /= 2


def on_sprite_2_click(
        e: ap.MouseEvent[ap.Sprite], options: Dict[str, Any]) -> None:
    """
    The handler would be called when a sprite is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    sprite: ap.Sprite = e.this
    sprite.y += 50


if __name__ == '__main__':
    main()
