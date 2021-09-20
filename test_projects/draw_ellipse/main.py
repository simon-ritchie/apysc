"""Test project for the draw_ellipse interface.

Command examples:
$ python test_projects/draw_ellipse/main.py
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
        background_color='#333',
        stage_width=1000, stage_height=500)
    sprite: ap.Sprite = ap.Sprite(stage=stage)

    sprite.graphics.begin_fill(color='#0af')
    ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
        x=50, y=25, width=100, height=50)
    ellipse.click(on_ellipse_click)

    sprite.graphics.begin_fill(color='')
    sprite.graphics.line_style(
        color='#fff', thickness=3, dot_setting=ap.LineDotSetting(dot_size=3))
    sprite.graphics.draw_ellipse(
        x=200, y=25, width=100, height=50)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_ellipse_click(
        e: ap.MouseEvent[ap.Ellipse], options: dict) -> None:
    """
    The handler would be called when the ellipse is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ellipse: ap.Ellipse = e.this
    ellipse.y += 50


if __name__ == '__main__':
    main()
