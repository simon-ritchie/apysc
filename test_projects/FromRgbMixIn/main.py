"""The test project for the `FromRgbMixIn` class.

Command examples:
$ python test_projects/FromRgbMixIn/main.py
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
    _: ap.Stage = ap.Stage(
        background_color=ap.Color("#333"),
        stage_width=1200,
        stage_height=900,
    )

    color: ap.Color = ap.Color.from_rgb(red=0, green=1, blue=2)
    ap.assert_equal(color, "#000102")

    color = ap.Color.from_rgb(red=255, green=255, blue=255)
    ap.assert_equal(color, "#FFFFFF")

    color = ap.Color.from_rgb(red=0, green=128, blue=255)
    ap.Rectangle(
        x=50,
        y=50,
        width=50,
        height=50,
        fill_color=color,
    )

    color = ap.Color.from_rgb(red=0, green=0, blue=0)
    ap.Rectangle(
        x=150,
        y=50,
        width=50,
        height=50,
        fill_color=color,
    )

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
