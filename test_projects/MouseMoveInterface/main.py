"""Test project for MouseMoveInterface class.

Command examples:
$ python test_projects/MouseMoveInterface/main.py
"""

import sys

sys.path.append('./')

import os
from types import ModuleType

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
    ap.Stage(
        background_color='#111',
        stage_width=1000, stage_height=500)
    sprite_1: ap.Sprite = ap.Sprite()
    sprite_1.graphics.begin_fill(color='#0af')

    rectangle_1: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    options: _MsgOptions = {'msg': 'Hello!'}
    rectangle_1.mousemove(
        handler=on_rectangle_1_mouse_move, options=options)

    rectangle_2: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=150, y=50, width=50, height=50)
    rectangle_2.mousemove(handler=on_rectangle_2_mouse_move)
    rectangle_2.unbind_mousemove(handler=on_rectangle_2_mouse_move)

    rectangle_3: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=250, y=50, width=50, height=50)
    rectangle_3.mousemove(handler=on_rectangle_3_mouse_move)
    rectangle_3.unbind_mousemove_all()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_rectangle_1_mouse_move(
        e: ap.MouseEvent, options: _MsgOptions) -> None:
    """
    Test handler that called when mouse is moved on rectangle_1.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('Mouse moved on rectangle 1!')
    ap.assert_equal(left='Hello!', right=options['msg'])


def on_rectangle_2_mouse_move(
        e: ap.MouseEvent, options: dict) -> None:
    """
    Test handler that called when mouse is moved on rectangle_2.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace(
        'Mouse moved on rectangle 2. Probably unbind_mousemove '
        'interface not working correctly.')


def on_rectangle_3_mouse_move(
        e: ap.MouseEvent, options: dict) -> None:
    """
    Test handler that called when mouse is moved on rectangle_3.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace(
        'Mouse moved on rectangle 3. Probably unbind_mousemove_all '
        'interface not working correctly.')


if __name__ == '__main__':
    main()
