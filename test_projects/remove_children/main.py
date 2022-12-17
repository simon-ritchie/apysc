"""A test project for the remove_children interface.

Command examples:
$ python test_projects/remove_children/main.py
"""

import os
import sys
from types import ModuleType
from typing import Optional

from typing_extensions import TypedDict

sys.path.append("./")

import apysc as ap
from apysc._display.child_mixin import ChildMixIn
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def _main() -> None:
    """
    Entry point of this test project.
    """
    ap.Stage(
        background_color="#333",
        stage_width=1000,
        stage_height=500,
        stage_elem_id="stage",
    )
    sprite_1: ap.Sprite = ap.Sprite()
    sprite_1.graphics.begin_fill(color="#0af")
    rectangle_1: ap.Rectangle = sprite_1.graphics.draw_rect(
        x=50, y=50, width=50, height=50
    )
    sprite_1.graphics.draw_rect(x=150, y=50, width=50, height=50)
    parent: Optional[ChildMixIn] = rectangle_1.parent
    if parent is not None:
        parent.remove_children()

    sprite_2: ap.Sprite = ap.Sprite()
    sprite_2.graphics.begin_fill(color="#f0a")
    rectangle_2: ap.Rectangle = sprite_2.graphics.draw_rect(
        x=50, y=150, width=50, height=50
    )
    sprite_2.graphics.draw_rect(x=150, y=150, width=50, height=50)
    options: _RectOptions = {"rectangle": rectangle_2}
    sprite_2.click(on_click, options=options)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_click(e: ap.MouseEvent, options: _RectOptions) -> None:
    """
    The click event handler.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : _RectOptions
        Optional arguments dictionary.
    """
    parent: Optional[ChildMixIn] = options["rectangle"].parent
    if parent is not None:
        parent.remove_children()


if __name__ == "__main__":
    _main()
