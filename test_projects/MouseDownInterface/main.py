"""Test project for MouseDownInterface class.

Command examples:
$ python test_projects/MouseDownInterface/main.py
$ python MouseDownInterface/main.py
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
    stage.mousedown(
        handler=on_stage_mouse_down,
        kwargs={'msg': 'Hello!'})

    sprite_1: Sprite = Sprite(stage=stage)
    sprite_1.mousedown(handler=on_sprite_1_mouse_down)

    sprite_1.graphics.begin_fill(color='#0af')
    rectangle_1: Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle_1.mousedown(handler=on_rectangle_1_mouse_down)

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


def on_stage_mouse_down(e: MouseEvent, kwargs: Dict[str, Any]) -> None:
    """
    Test handler that called when stage is mouse downed.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    kwargs : dict
        Specified keyword arguments.
    """
    trace('Stage is mouse downed!')
    assert_equal(expected='Hello!', actual=kwargs['msg'])


def on_sprite_1_mouse_down(e: MouseEvent, kwargs: Dict[str, Any]) -> None:
    """
    Test handler that called when sprite 1 is mouse downed.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    kwargs : dict
        Specified keyword arguments.
    """
    trace('Sprite 1 is mouse downed!')


def on_rectangle_1_mouse_down(e: MouseEvent, kwargs: Dict[str, Any]) -> None:
    """
    Test handler that called when rectangle 1 is mouse downed.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    kwargs : dict
        Specified keyword arguments.
    """
    trace('Rectangle 1 is mouse downed!')


if __name__ == '__main__':
    main()
