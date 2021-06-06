"""Test project for the draw_circle interface.

Command examples:
$ python test_projects/draw_circle/main.py
$ python draw_circle/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

from apysc import Int, Circle
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

    sprite.graphics.begin_fill(color='0af')
    sprite.graphics.draw_circle(x=75, y=75, radius=50)

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


if __name__ == '__main__':
    main()
