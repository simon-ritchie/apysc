"""The test project for the RotateAroundCenterInterface.

Command examples:
$ python test_projects/RotateAroundCenterInterface/main.py
$ python RotateAroundCenterInterface/main.py
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

    sprite.graphics.begin_fill(color='#0af', alpha=0.5)
    rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle_1.rotate_around_center(30)

    sprite.graphics.begin_fill(color='#f0a', alpha=0.5)
    rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle_2.rotate_around_center(30)
    rectangle_2.rotate_around_center(30)

    sprite.click(on_sprite_click, options={'rectangle_1': rectangle_1})

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_sprite_click(
        e: ap.MouseEvent[ap.Sprite], options: Dict[str, Any]) -> None:
    """
    The handler would be called when the sprite is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle_1: ap.Rectangle = options['rectangle_1']
    rectangle_1.rotate_around_center(10)


if __name__ == '__main__':
    main()
