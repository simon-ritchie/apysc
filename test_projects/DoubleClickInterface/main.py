"""Test project for DoubleClickInterface class.

Command examples:
$ python test_projects/DoubleClickInterface/main.py
$ python DoubleClickInterface/main.py
"""

import sys
from typing import Any
from typing import Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import Event, MouseEvent
from apysc import Rectangle
from apysc import Sprite
from apysc import Stage
from apysc import String
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
    stage.dblclick(
        handler=on_stage_dblclick,
        kwargs={'msg': String('Hello!')})

    sprite_1: Sprite = Sprite(stage=stage)
    sprite_1.dblclick(handler=on_sprite_1_dblclick)

    sprite_1.graphics.begin_fill(color='#0af')
    rectangle_1: Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    rectangle_1.dblclick(handler=on_rectangle_1_dblclick)

    exporter.save_expressions_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


def on_stage_dblclick(e: MouseEvent, kwargs: Dict[str, Any]) -> None:
    """
    Test handler that called when staget is double clicked.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    kwargs : dict
        Specified keyword arguments.
    """
    trace('Stage is double clicked!')
    assert_equal(expected='Hello!', actual=kwargs['msg'])


def on_sprite_1_dblclick(e: MouseEvent, kwargs: Dict[str, Any]) -> None:
    """
    Test handler that called when sprite_1 is double clicked.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    kwargs : dict
        Specified keyword arguments.
    """
    trace('Sprite 1 is double clicked!')


def on_rectangle_1_dblclick(e: MouseEvent, kwargs: Dict[str, Any]) -> None:
    """
    Test handler that called when rectangle_1 is double clicked.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    kwargs : dict
        Specified keyword arguments.
    """
    trace('Rectangle 1 is double clicked!')


if __name__ == '__main__':
    main()
