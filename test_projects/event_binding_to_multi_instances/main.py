"""The test project to check the behavior of the binding
same handler multiple times.

Command examples:
$ python test_projects/event_binding_to_multi_instances/main.py
$ python event_binding_to_multi_instances/main.py
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
    sprite.graphics.begin_fill(color='#0af')
    rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle_1.click(on_click)
    rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
        x=150, y=50, width=50, height=50)
    rectangle_2.click(on_click)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_click(e: ap.MouseEvent[ap.Rectangle], options: Dict[Any, Any]) -> None:
    """
    The handler would be called when a rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    ap.trace(rectangle.x)


if __name__ == '__main__':
    main()
