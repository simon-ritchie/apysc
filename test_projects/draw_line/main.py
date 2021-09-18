"""Test project for draw_line interface.

Command examples:
$ python test_projects/draw_line/main.py
$ python draw_line/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType
from typing import Any
from typing import Dict

from typing_extensions import TypedDict

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


class _SpOptions(TypedDict):
    sprite: ap.Sprite


def main() -> None:
    """
    Entry point of this test project.
    """
    stage: ap.Stage = ap.Stage(
        background_color='#333',
        stage_width=1000, stage_height=500)
    sprite: ap.Sprite = ap.Sprite(stage=stage)
    sprite.graphics.line_style(
        color='#0af', thickness=5, dot_setting=ap.LineDotSetting(dot_size=10))
    _: ap.Line = sprite.graphics.draw_line(
        x_start=50, y_start=50, x_end=350, y_end=50)

    sprite.graphics.line_style(
        color='#0af', thickness=10, cap=ap.LineCaps.ROUND)
    line_2: ap.Line = sprite.graphics.draw_line(
        x_start=50, y_start=80, x_end=350, y_end=80)
    options: _SpOptions = {'sprite': sprite}
    line_2.click(on_line_click, options=options)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_line_click(
        e: ap.MouseEvent[ap.Line], options: _SpOptions) -> None:
    """
    Handler that called when line is clicked.

    Parameters
    ----------
    e : MouseEvent
        Created MouseEvent instance.
    options : dict
        Optional parameters.
    """
    sprite: ap.Sprite = options['sprite']
    sprite.x += 100


if __name__ == '__main__':
    main()
