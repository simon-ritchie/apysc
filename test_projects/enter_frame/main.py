"""The test project for the `enter_frame` interface.

Command examples:
$ python test_projects/enter_frame/main.py
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
    _: ap.Stage = ap.Stage(background_color="#333")
    sprite: ap.Sprite = ap.Sprite()
    sprite.enter_frame(handler=on_enter_frame)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_enter_frame(e: ap.EnterFrameEvent[ap.Sprite], options: dict) -> None:
    ap.trace(ap.DateTime.now(), e.this)


if __name__ == "__main__":
    main()
