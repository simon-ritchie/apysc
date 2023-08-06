"""Test project for DoubleClickMixIn class.

Command examples:
$ python test_projects/DoubleClickMixIn/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

from typing_extensions import TypedDict

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


class _MsgOptions(TypedDict):
    msg: str


def main() -> None:
    """Entry point of this test project."""
    ap.Stage(background_color=ap.Color("#111"), stage_width=1000, stage_height=500)
    sprite_1: ap.Sprite = ap.Sprite()
    sprite_1.graphics.begin_fill(color=ap.Color("#0af"))

    rectangle_1: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50
    )
    options: _MsgOptions = {"msg": "Hello!"}
    rectangle_1.dblclick(handler=on_rectangle_1_dblclick, options=options)

    rectangle_2: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=150, y=50, width=50, height=50
    )
    rectangle_2.dblclick(handler=on_rectangle_2_dblclick)
    rectangle_2.unbind_dblclick(handler=on_rectangle_2_dblclick)

    rectangle_3: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=250, y=50, width=50, height=50
    )
    rectangle_3.dblclick(handler=on_rectangle_3_dblclick)
    rectangle_3.unbind_dblclick_all()

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_rectangle_1_dblclick(e: ap.MouseEvent, options: _MsgOptions) -> None:
    """
    Test handler that called when rectangle_1 is double clicked.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace("Rectangle 1 is double clicked!")
    ap.assert_equal(left="Hello!", right=options["msg"])


def on_rectangle_2_dblclick(e: ap.MouseEvent, options: dict) -> None:
    """
    Test handler that called when rectangle 2 is double clicked.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace(
        "Rectangle 2 is double clicked. Probably unbind_dblclick "
        "interface not working correctly."
    )


def on_rectangle_3_dblclick(e: ap.MouseEvent, options: dict) -> None:
    """
    Test handler that called when rectangle 3 is double clicked.

    Parameters
    ----------
    e : MouseEvent
        Event object.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace(
        "Rectangle 3 is double clicked. Probably unbind_dblclick_all "
        "interface not working correctly."
    )


if __name__ == "__main__":
    main()
