"""Test project for MouseEvent class.

Command examples:
$ python test_projects/MouseEvent/main.py
$ python MouseEvent/main.py
"""

import sys
from typing import Any, Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import Int, MouseEvent
from apysc import Number
from apysc import Rectangle
from apysc import Sprite
from apysc import Stage
from apysc import String
from apysc import assert_not_equal, assert_true
from apysc.file import file_util
from apysc.html import exporter
from apysc.expression import expression_file_util
from apysc import trace

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
    expression_file_util.append_js_expression(
        f'{stage_elem_str}.css("margin-left", "150px");')

    sprite_1: Sprite = Sprite(stage=stage)
    sprite_1.graphics.begin_fill(color='#0af')
    rectangle_1: Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle_1.click(on_rectangle_1_clicked)

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_rectangle_1_clicked(e: MouseEvent, kwargs: Dict[str, Any]) -> None:
    """
    Test handler that called when rectangle_1 is clicked.

    Parameters
    ----------
    e : Event
        Event object.
    kwargs : dict
        Specified keyword arguments.
    """
    trace('Rectangle 1 clicked!')
    trace('stage_x:', e.stage_x)
    assert_true(e.stage_x >= Int(50))
    assert_true(e.stage_x <= Int(100))


if __name__ == '__main__':
    main()
