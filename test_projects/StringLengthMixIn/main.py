"""The test project for the `StringLengthMixIn` class.

Command examples:
$ python test_projects/StringLengthMixIn/main.py
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

    string: ap.String = ap.String("abc")
    ap.assert_equal(string.length, 3)

    string = ap.String("あいうえお")
    ap.assert_equal(string.length, 5)

    string = ap.String("𩸽")
    ap.assert_equal(string.length, 1)

    string = ap.String("😀")
    ap.assert_equal(string.length, 1)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
