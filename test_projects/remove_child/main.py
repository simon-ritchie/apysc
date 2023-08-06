"""Test project for `remove_child` interface.

Command examples:
$ python test_projects/remove_child/main.py
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
    stage: ap.Stage = ap.Stage(
        background_color=ap.Color("#333"), stage_width=1000, stage_height=500
    )

    sprite_1: ap.Sprite = ap.Sprite()
    sprite_1.graphics.begin_fill(color=ap.Color("#666"))
    sprite_1.graphics.draw_rect(x=50, y=50, width=100, height=100)
    stage.add_child(sprite_1)

    sprite_2: ap.Sprite = ap.Sprite()
    sprite_2.graphics.begin_fill(color=ap.Color("#666"))
    sprite_2.graphics.draw_rect(x=150, y=50, width=100, height=100)
    stage.add_child(sprite_2)
    stage.remove_child(child=sprite_2)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == "__main__":
    main()
