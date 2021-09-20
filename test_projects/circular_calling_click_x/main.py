"""The test project for the mouse event circular calling and
updating x-coordinate interface value.

Command examples:
$ python test_projects/circular_calling_click_x/main.py
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
        stage_width=1000, stage_height=500, stage_elem_id='stage')
    sprite: ap.Sprite = ap.Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#00aaff')

    rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle.click(on_click_1)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_click_1(
        e: ap.MouseEvent[ap.Rectangle], options: Dict[Any, Any]) -> None:
    """
    The handler will be called when the rectangle is clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.x += 50
    e.this.unbind_click(on_click_1)
    e.this.click(on_click_2)


def on_click_2(
        e: ap.MouseEvent[ap.Rectangle], options: Dict[Any, Any]) -> None:
    """
    The handler will be called when the rectangle is clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.x -= 50
    e.this.unbind_click(on_click_2)
    e.this.click(on_click_1)


if __name__ == '__main__':
    main()
