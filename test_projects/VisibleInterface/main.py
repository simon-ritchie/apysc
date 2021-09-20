"""Test project for VisibleInterface class.

Command examples:
$ python test_projects/VisibleInterface/main.py
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


class _Options(TypedDict):
    sprite_2: ap.Sprite
    rectangle_3: ap.Rectangle
    rectangle_4: ap.Rectangle


def main() -> None:
    """
    Entry point of this test project.
    """
    stage: ap.Stage = ap.Stage(background_color='#333', stage_height=300)

    sprite_1: ap.Sprite = ap.Sprite(stage=stage)
    sprite_1.graphics.begin_fill(color='#0af')
    rectangle_1: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle_2: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=150, y=50, width=50, height=50)
    rectangle_2.visible = ap.Boolean(False)

    sprite_2: ap.Sprite = ap.Sprite(stage=stage)
    sprite_2.graphics.begin_fill(color='#f0a')
    rectangle_3: ap.Rectangle = sprite_2.graphics.draw_rect(
        x=50, y=150, width=50, height=50)
    rectangle_4: ap.Rectangle = sprite_2.graphics.draw_rect(
        x=150, y=150, width=50, height=50)
    sprite_2.visible = ap.Boolean(False)

    options: _Options = {
        'sprite_2': sprite_2,
        'rectangle_3': rectangle_3,
        'rectangle_4': rectangle_4}
    rectangle_1.click(
        on_rectangle_1_click,
        options=options)
    rectangle_3.click(on_rectangle_3_or_4_click)
    rectangle_4.click(on_rectangle_3_or_4_click)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_rectangle_1_click(e: ap.MouseEvent, options: _Options) -> None:
    """
    Handler that called when rectangle_1 is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional values.
    """
    sprite_2: ap.Sprite = options['sprite_2']
    sprite_2.visible = ap.Boolean(True)
    rectangle_3: ap.Rectangle = options['rectangle_3']
    rectangle_3.visible = ap.Boolean(True)
    rectangle_4: ap.Rectangle = options['rectangle_4']
    rectangle_4.visible = ap.Boolean(True)


def on_rectangle_3_or_4_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    Handler that called when rectangle_3 or rectangle_4 is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional values.
    """
    e.this.visible = ap.Boolean(False)


if __name__ == '__main__':
    main()
