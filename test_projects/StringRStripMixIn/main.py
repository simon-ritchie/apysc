"""The test project for the `StringRStripMixIn` class.

Command examples:
$ python test_projects/StringRStripMixIn/main.py
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
        background_color="#333",
        stage_width=1200,
        stage_height=900,
    )

    string: ap.String = ap.String(" 　\n aabbccaa \n　 ")
    string = string.rstrip()
    ap.assert_equal(string, " 　\n aabbccaa")

    string: ap.String = ap.String("aabbccaa")
    string = string.rstrip(string="a")
    ap.assert_equal(string, "aabbcc")

    string: ap.String = ap.String("aabbccaa")
    string = string.rstrip(string=ap.String("a"))
    ap.assert_equal(string, "aabbcc")

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
