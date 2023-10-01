"""Test project for `GreenColorMixIn` class.

Command examples:
$ python test_projects/GreenColorMixIn/main.py
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
    _: ap.Stage = ap.Stage(background_color=ap.Color("#333"))

    color: ap.Color = ap.Color("#a0f")
    green_color: ap.Int = color.green_color
    ap.assert_equal(green_color, 0)

    color = ap.Color("#000100")
    green_color = color.green_color
    ap.assert_equal(green_color, 1)

    color = ap.Color("#0fa")
    green_color = color.green_color
    ap.assert_equal(green_color, 255)

    color = ap.Color("#00fe00")
    green_color = color.green_color
    ap.assert_equal(green_color, 254)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == "__main__":
    main()
