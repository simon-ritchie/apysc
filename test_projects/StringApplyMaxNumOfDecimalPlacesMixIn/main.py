"""The test project for the `StringApplyMaxNumOfDecimalPlacesMixIn` class.

Command examples:
$ python test_projects/StringApplyMaxNumOfDecimalPlacesMixIn/main.py
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

    string: ap.String = ap.String("abc")
    string = string.apply_max_num_of_decimal_places(
        max_num_of_decimal_places=ap.Int(3),
    )
    ap.assert_equal(string, "abc")

    string = ap.String("123.456.789.012")
    string = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=ap.Int(1))
    ap.assert_equal(string, "123.456.789.012")

    string = ap.String("123.456")
    string = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=1)
    ap.assert_equal(string, "123.4")

    string = ap.String("123.456")
    string = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=ap.Int(2))
    ap.assert_equal(string, "123.45")

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
