"""Test project for MouseOutInterface class.

Command examples:
$ python test_projects/MouseOutInterface/main.py
$ python MouseOutInterface/main.py
"""

import sys
from typing import Any
from typing import Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import MouseEvent
from apysc import Rectangle
from apysc import Sprite
from apysc import Stage
from apysc import assert_equal
from apysc import trace
from apysc.file import file_util
from apysc.html import exporter

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module),
    'test_output/'
)


def main() -> None:
    """Entry point of this test project.
    """
    stage: Stage = Stage(
        background_color='#111',
        stage_width=1000, stage_height=500)
    sprite_1: Sprite = Sprite(stage=stage)
    sprite_1.graphics.begin_fill(color='#0af')

    rectangle_1: Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle_1.mouseout(
        handler=on_rectangle_1_mouse_out, options={'msg': 'Hello!'})

    rectangle_2: Rectangle = sprite_1.graphics.draw_rect(
        x=150, y=50, width=50, height=50)
    rectangle_2.mouseout(handler=on_rectangle_2_mouse_out)
    rectangle_2.unbind_mouseout(handler=on_rectangle_2_mouse_out)

    rectangle_3: Rectangle = sprite_1.graphics.draw_rect(
        x=250, y=50, width=50, height=50)
    rectangle_3.mouseout(handler=on_rectangle_3_mouse_out)
    rectangle_3.unbind_mouseout_all()

    exporter.save_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


def on_rectangle_1_mouse_out(e: MouseEvent, options: Dict[str, Any]) -> None:
    """
    Test handler that called when rectangle 1 is mouse outed.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace('Rectangle 1 is mouse outed!')
    assert_equal(expected='Hello!', actual=options['msg'])


def on_rectangle_2_mouse_out(e: MouseEvent, options: Dict[str, Any]) -> None:
    """
    Test handler that called when rectangle 2 is mouse outed.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace(
        'Rectangle 2 is mouse outed. Probably unbind_mouseout '
        'interface not working correctly.')


def on_rectangle_3_mouse_out(e: MouseEvent, options: Dict[str, Any]) -> None:
    """
    Test handler that called when rectanble 3 is mouse outed.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace(
        'Rectangle 3 is mouse outed. Probably unbind_mouseout_all '
        'interface not working correctly.')


if __name__ == '__main__':
    main()
