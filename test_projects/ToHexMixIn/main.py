"""The test project for the `ToHexMixIn` class.

Command examples:
$ python test_projects/ToHexMixIn/main.py
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

    inteter: ap.Int = ap.Int(0)
    hex_str: ap.String = inteter.to_hex()
    ap.assert_equal(hex_str, "0")

    inteter = ap.Int(15)
    hex_str = inteter.to_hex()
    ap.assert_equal(hex_str, "f")

    inteter = ap.Int(16)
    hex_str = inteter.to_hex()
    ap.assert_equal(hex_str, "10")

    number: ap.Number = ap.Number(0)
    hex_str = number.to_hex()
    ap.assert_equal(hex_str, "0")

    number = ap.Number(15.5)
    hex_str = number.to_hex()
    ap.assert_equal(hex_str, "f")

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
