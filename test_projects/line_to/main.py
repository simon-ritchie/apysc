"""Test project for line_to interface.

Command examples:
$ python test_projects/line_to/main.py
$ python line_to/main.py
"""

import sys

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
        background_color='#111',
        stage_width=1000, stage_height=500)

    sprite: ap.Sprite = ap.Sprite(stage=stage)
    sprite.graphics.begin_fill(color='#0af', alpha=0.5)
    sprite.graphics.line_style(color='#eee', thickness=4, alpha=0.75)
    sprite.graphics.line_to(x=100, y=0)
    sprite.graphics.line_to(x=100, y=100)
    sprite.graphics.line_to(x=0, y=0)

    sprite.graphics.begin_fill(color='#f0a', alpha=0.5)
    sprite.graphics.move_to(x=100, y=100)
    sprite.graphics.line_to(x=100, y=200)
    sprite.graphics.line_to(x=200, y=200)
    sprite.graphics.line_to(x=100, y=100)

    sprite.graphics.move_to(x=ap.Int(0), y=ap.Int(0))
    sprite.graphics.line_to(x=ap.Int(100), y=ap.Int(0))
    polyline: ap.Polyline = sprite.graphics.line_to(
        x=ap.Int(100), y=ap.Int(100))
    polyline.x = ap.Int(200)
    polyline.y = ap.Int(200)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == '__main__':
    main()
