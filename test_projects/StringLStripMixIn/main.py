"""The test project for the `StringLStripMixIn` class.

Command examples:
$ python test_projects/StringLStripMixIn/main.py
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

    string: ap.String = ap.String("  　　\naabbcc  ")
    string = string.lstrip()
    ap.assert_equal(string, "aabbcc  ")

    string = ap.String("aabbccaa")
    string = string.lstrip(string="a")
    ap.assert_equal(string, "bbccaa")

    string = ap.String("aabbccaa")
    string = string.lstrip(string=ap.String("a"))
    ap.assert_equal(string, "bbccaa")

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
