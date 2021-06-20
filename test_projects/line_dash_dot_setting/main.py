"""Test project for line_dash_dot_setting.

Command examples:
$ python test_projects/line_dash_dot_setting/main.py
$ python line_dash_dot_setting/main.py
"""

import sys
from typing import Any
from typing import Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import LineDashDotSetting
from apysc import MouseEvent
from apysc import Polyline
from apysc import Sprite
from apysc import Stage
from apysc import save_overall_html
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
    stage: Stage = Stage(
        background_color='#333',
        stage_width=1000, stage_height=500)

    sprite: Sprite = Sprite(stage=stage)
    sprite.graphics.line_style(
        color='#0af',
        thickness=2,
        dash_dot_setting=LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=5))
    sprite.graphics.move_to(x=50, y=30)
    sprite.graphics.line_to(x=450, y=30)

    sprite.graphics.line_style(
        color='#0af',
        thickness=2,
        dash_dot_setting=LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=10))
    sprite.graphics.move_to(x=50, y=60)
    sprite.graphics.line_to(x=450, y=60)

    sprite.graphics.line_style(
        color='#0af',
        thickness=2)
    sprite.graphics.move_to(x=50, y=90)
    sprite.graphics.line_to(x=450, y=90)

    sprite.graphics.line_style(
        color='#0af',
        thickness=2,
        dash_dot_setting=LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=5))
    polyline: Polyline = sprite.graphics.move_to(x=50, y=120)
    sprite.graphics.line_to(x=450, y=120)
    sprite.graphics.line_to(x=650, y=200)
    polyline.click(on_polyline_click)

    save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_polyline_click(
        e: MouseEvent[Polyline], options: Dict[str, Any]) -> None:
    """
    Handler that called when polyline is clicked.

    Parameters
    ----------
    e : MouseEvent
        Created MouseEvent instance.
    options : dict
        Optional parameters.
    """
    polyline: Polyline = e.this
    polyline.line_dash_dot_setting = None


if __name__ == '__main__':
    main()
