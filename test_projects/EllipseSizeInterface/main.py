"""Test project for EllipseSizeInterface class.

Command examples:
$ python test_projects/EllipseSizeInterface/main.py
$ python EllipseSizeInterface/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc import Int
from apysc import Rectangle
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
    sprite.graphics.begin_fill(color='#0af')

    rectangle_1: Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle_1.ellipse_size = Int(10)

    rectangle_2: Rectangle = sprite.graphics.draw_rect(
        x=150, y=50, width=50, height=50)
    rectangle_2.ellipse_size = Int(20)

    rectangle_3: Rectangle = sprite.graphics.draw_rect(
        x=250, y=50, width=50, height=50)
    rectangle_3.ellipse_width = Int(10)
    rectangle_3.ellipse_height = Int(25)

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == '__main__':
    main()
