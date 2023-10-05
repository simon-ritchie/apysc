"""The test project for the `RedColorMixIn` class.

Command examples:
$ python test_projects/RedColorMixIn/main.py
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

    color: ap.Color = ap.Color("#0af")
    red_color: ap.Int = color.red_color
    ap.assert_equal(red_color, 0)

    color = ap.Color("#010000")
    red_color = color.red_color
    ap.assert_equal(red_color, 1)

    color = ap.Color("#fa0")
    red_color = color.red_color
    ap.assert_equal(red_color, 255)

    color = ap.Color("#fe0000")
    red_color = color.red_color
    ap.assert_equal(red_color, 254)

    color.red_color = ap.Int(0)
    red_color = color.red_color
    ap.assert_equal(red_color, 0)

    color.red_color = ap.Int(255)
    red_color = color.red_color
    ap.assert_equal(red_color, 255)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == "__main__":
    main()
