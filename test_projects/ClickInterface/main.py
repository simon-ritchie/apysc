"""Test project for ClickInterface class.

Command examples:
$ python test_projects/ClickInterface/main.py
$ python ClickInterface/main.py
"""

import sys
from typing import Any
from typing import Dict

sys.path.append('./')

import os
from types import ModuleType

from apysc import Event
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
    """
    Entry point of this test project.
    """
    stage: Stage = Stage(
        background_color='#111',
        stage_width=1000, stage_height=500)
    stage.click(on_stage_clicked)

    sprite_1: Sprite = Sprite(stage=stage)
    sprite_1.graphics.begin_fill(color='#0af')
    rectangle_1: Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50)
    msg: String = String('Hello!')
    sprite_1.click(on_sprite_1_clicked, options={'msg': msg})
    rectangle_1.click(on_rectangle_1_clicked)

    sprite_2: Sprite = Sprite(stage=stage)
    sprite_2.graphics.begin_fill(color='#f0a')
    sprite_2.click(on_sprite_2_clicked)
    rectangle_2: Rectangle = sprite_2.graphics.draw_rect(
        x=150, y=50, width=50, height=50)
    rectangle_2.click(on_rectangle_2_clicked)

    rectangle_3: Rectangle = sprite_2.graphics.draw_rect(
        x=250, y=50, width=50, height=50)
    rectangle_3.click(on_rectangle_3_clicked)

    rectangle_4: Rectangle = sprite_2.graphics.draw_rect(
        x=350, y=50, width=50, height=50)
    rectangle_4.click(on_rectangle_4_1_clicked)
    rectangle_4.click(on_rectangle_4_2_clicked)

    exporter.save_overall_html(
        dest_dir_path=_DEST_DIR_PATH)


def on_stage_clicked(e: Event, options: Dict[str, Any]) -> None:
    """
    Test handler that called when stage is clicked.

    Parameters
    ----------
    e : Event
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace('Stage is clicked!')


def on_sprite_1_clicked(e: Event, options: Dict[str, Any]) -> None:
    """
    Test handler that called when sprite_1 is clicked.

    Parameters
    ----------
    e : Event
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace('Sprite 1 is clicked!')
    assert_equal(expected='Hello!', actual=options['msg'])


def on_sprite_2_clicked(e: Event, options: Dict[str, Any]) -> None:
    """
    Test handler that called when sprite_2 is clicked.

    Parameters
    ----------
    e : Event
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace('Sprite 2 is clicked!')


def on_rectangle_1_clicked(e: Event, options: Dict[str, Any]) -> None:
    """
    Test handler that called when rectangle_1 is clicked.

    Parameters
    ----------
    e : Event
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace('Rectangle 1 is clicked!')


def on_rectangle_2_clicked(e: Event, options: Dict[str, Any]) -> None:
    """
    Test handler that called when rectangle_2 is clicked.

    Parameters
    ----------
    e : Event
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace('Rectangle 2 is clicked!')
    e.prevent_default()
    e.stop_propagation()


def on_rectangle_3_clicked(
        e: Event[Rectangle], options: Dict[str, Any]) -> None:
    """
    Test handler that called when rectangle_3 is clicked.

    Parameters
    ----------
    e : Event
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace('Rectangle 3 is clicked and event is unbinded!')
    e.this.unbind_click(handler=on_rectangle_3_clicked)
    e.stop_propagation()
    e.prevent_default()


def on_rectangle_4_1_clicked(
        e: Event[Rectangle], options: Dict[str, Any]) -> None:
    """
    Test handler that called when rectangle_4 is clicked.

    Parameters
    ----------
    e : Event
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace('Rectangle 4 is clicked!')


def on_rectangle_4_2_clicked(
        e: Event[Rectangle], options: Dict[str, Any]) -> None:
    """
    Test handler that called when rectangle_4 is clicked.

    Parameters
    ----------
    e : Event
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    trace('Rectangle 4 is clicked and all click events are unbinded!')
    e.this.unbind_click_all()


if __name__ == '__main__':
    main()
