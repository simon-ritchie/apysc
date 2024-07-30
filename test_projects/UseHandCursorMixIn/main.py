"""Test project for the `UseHandCursorMixIn` class.

Command examples:
$ python test_projects/UseHandCursorMixIn/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

import env_var_util

env_var_util.apply_material_icons_import_skipping_setting()

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
    _: ap.Stage = ap.Stage(
        background_color=ap.Color("#333"),
        stage_width=1200,
        stage_height=900,
    )

    sprite: ap.Sprite = ap.Sprite()
    sprite.use_hand_cursor = ap.True_
    sprite.click(_on_sprite_click)
    ap.Rectangle(
        x=50,
        y=50,
        width=50,
        height=50,
        fill_color=ap.Colors.CYAN_00AAFF,
        parent=sprite,
    )

    rectangle: ap.Rectangle = ap.Rectangle(
        x=50,
        y=150,
        width=50,
        height=50,
        fill_color=ap.Colors.CYAN_00AAFF,
    )
    rectangle.use_hand_cursor = ap.True_

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def _on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:
    """
    Handler that called when a sprite is clicked.

    Parameters
    ----------
    e : MouseEvent
        A created MouseEvent instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.use_hand_cursor = ap.False_


if __name__ == "__main__":
    main()
