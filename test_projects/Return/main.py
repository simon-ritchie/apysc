"""The test project for the `Return` class.

Command examples:
$ python test_projects/Return/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

import apysc as ap
from apysc._file import file_util

this_module: ModuleType = sys.modules[__name__]

_DEST_DIR_PATH: str = os.path.join(
    file_util.get_abs_module_dir_path(module=this_module), "test_output/"
)


def main() -> None:
    """
    Entry point of this test project.
    """
    ap.Stage(
        background_color=ap.Color("#333"),
        stage_width=1000,
        stage_height=500,
        stage_elem_id="stage",
    )
    sprite: ap.Sprite = ap.Sprite()
    sprite.graphics.begin_fill(color=ap.Color("#0af"))
    rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
    rectangle.click(on_rectangle_click)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_rectangle_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the rectangle is clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    fill_color: ap.Color = e.this.fill_color
    condition: ap.Boolean = fill_color == ap.Color("#00aaff")
    with ap.If(condition):
        e.this.fill_color = ap.Color("#f0a")
        ap.Return()

    condition = fill_color == ap.Color("#ff00aa")
    with ap.If(condition):
        e.this.fill_color = ap.Color("#0fa")
        ap.Return()

    condition = fill_color == ap.Color("#00ffaa")
    with ap.If(condition):
        e.this.fill_color = ap.Color("#0af")
        ap.Return()


if __name__ == "__main__":
    main()
