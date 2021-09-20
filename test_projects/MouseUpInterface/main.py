"""Test project for MouseUpInterface class.

Command examples:
$ python test_projects/MouseUpInterface/main.py
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


class _MsgOptions(TypedDict):
    msg: str


def main() -> None:
    """Entry point of this test project.
    """
    stage: ap.Stage = ap.Stage(
        background_color='#111',
        stage_width=1000, stage_height=500)
    sprite_1: ap.Sprite = ap.Sprite(stage=stage)
    sprite_1.graphics.begin_fill(color='#0af')

    rectangle_1: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    options: _MsgOptions = {'msg': 'Hello!'}
    rectangle_1.mouseup(on_rectangle_1_mouse_up, options=options)

    rectangle_2: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=150, y=50, width=50, height=50)
    rectangle_2.mouseup(on_rectangle_2_mouse_up)
    rectangle_2.unbind_mouseup(handler=on_rectangle_2_mouse_up)

    rectangle_3: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=250, y=50, width=50, height=50)
    rectangle_3.mouseup(on_rectangle_3_mouse_up)
    rectangle_3.unbind_mouseup_all()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_rectangle_1_mouse_up(
        e: ap.MouseEvent, options: _MsgOptions) -> None:
    """
    Test handler that called when rectangle 1 is mouse upped.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('Rectangle 1 is mouse upped!')
    ap.assert_equal(expected='Hello!', actual=options['msg'])


def on_rectangle_2_mouse_up(
        e: ap.MouseEvent, options: Dict[Any, Any]) -> None:
    """
    Test handler that called when rectangle 2 is mouse upped.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace(
        'Rectangle 2 is mouse upped. Probably unbind_mouseup '
        'interface not working correctly.')


def on_rectangle_3_mouse_up(
        e: ap.MouseEvent, options: Dict[Any, Any]) -> None:
    """
    Test handler that called when rectangle 3 is mouse upped.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace(
        'Rectangle 3 is mouse upped. Probably unbind_mouseup_all '
        'interface not working correctly.')


if __name__ == '__main__':
    main()
