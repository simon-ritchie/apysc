"""Test project for MouseEvent class.

Command examples:
$ python test_projects/MouseEvent/main.py
$ python MouseEvent/main.py
"""

import sys
from typing import Any
from typing import Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import Int
from apysc import MouseEvent
from apysc import Rectangle
from apysc import Sprite
from apysc import Stage
from apysc import assert_true
from apysc import save_overall_html
from apysc import trace
from apysc import append_js_expression
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
    stage_elem_id: str = stage.stage_elem_id
    stage_elem_str: str = f'$("#{stage_elem_id}")'
    append_js_expression(
        f'{stage_elem_str}.css("margin-left", "150px");')

    sprite_1: Sprite = Sprite(stage=stage)
    sprite_1.graphics.begin_fill(color='#0af')
    rectangle_1: Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=100, width=50, height=50)
    rectangle_1.click(on_rectangle_1_clicked)

    sprite_2: Sprite = Sprite(stage=stage)
    sprite_2.graphics.begin_fill(color='#f0a')
    sprite_2.x = Int(150)
    sprite_2.y = Int(100)
    rectangle_2: Rectangle = sprite_2.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle_2.click(on_rectangle_2_clicked)

    save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_rectangle_1_clicked(e: MouseEvent, options: Dict[str, Any]) -> None:
    """
    Test handler that called when rectangle_1 is clicked.

    Parameters
    ----------
    e : Event
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace('Rectangle 1 clicked!')
    trace('stage_x:', e.stage_x)
    assert_true(e.stage_x >= Int(50))
    assert_true(e.stage_x <= Int(100))

    trace('stage_y:', e.stage_y)
    assert_true(e.stage_y >= Int(100))
    assert_true(e.stage_y <= Int(150))

    trace('local_x:', e.local_x)
    assert_true(e.local_x >= Int(0))
    assert_true(e.local_x <= Int(50))


def on_rectangle_2_clicked(e: MouseEvent, options: Dict[str, Any]) -> None:
    """
    Test handler that called when rectangle_2 is clicked.

    Parameters
    ----------
    e : Event
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace('Rectangle 2 clicked!')
    trace('local_x:', e.local_x)
    assert_true(e.local_x >= Int(0))
    assert_true(e.local_x <= Int(50))

    trace('local_y:', e.local_y)
    assert_true(e.local_y >= Int(0))
    assert_true(e.local_y <= Int(50))


if __name__ == '__main__':
    main()
