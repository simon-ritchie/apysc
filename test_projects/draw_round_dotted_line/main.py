"""Test project for draw_round_dotted_line interface.

Command examples:
$ python test_projects/draw_round_dotted_line/main.py
$ python draw_round_dotted_line/main.py
"""

import sys
from typing import Any
from typing import Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import Line
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
    sprite.graphics.line_style(
        color='#0af', thickness=10, dot_setting=LineDotSetting(dot_size=3))
    _: Line = sprite.graphics.draw_round_dotted_line(
        x_start=50, y_start=50, x_end=350, y_end=50,
        round_size=10, space_size=5)

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)

if __name__ == '__main__':
    main()
