"""The test project for the `StringSliceMixIn` class.

Command examples:
$ python test_projects/StringSliceMixIn/main.py
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

    string: ap.String = ap.String("012345")
    result_string: ap.String = string.slice(start=0)
    ap.assert_equal("012345", result_string)
    result_string = string.slice(start=ap.Int(0))
    ap.assert_equal("012345", result_string)

    result_string = string.slice(start=1)
    ap.assert_equal("12345", result_string)
    result_string = string.slice(start=ap.Int(1))
    ap.assert_equal("12345", result_string)

    result_string = string.slice(start=2)
    ap.assert_equal("2345", result_string)
    result_string = string.slice(start=ap.Int(2))
    ap.assert_equal("2345", result_string)

    result_string = string.slice(start=0, end=2)
    ap.assert_equal("01", result_string)
    result_string = string.slice(start=ap.Int(0), end=ap.Int(2))
    ap.assert_equal("01", result_string)

    result_string = string.slice(start=2, end=4)
    ap.assert_equal("23", result_string)
    result_string = string.slice(start=ap.Int(2), end=ap.Int(4))
    ap.assert_equal("23", result_string)

    result_string = string.slice(start=-2)
    ap.assert_equal("45", result_string)
    result_string = string.slice(start=ap.Int(-2))
    ap.assert_equal("45", result_string)

    result_string = string.slice(start=-3, end=-1)
    ap.assert_equal("34", result_string)
    result_string = string.slice(start=ap.Int(-3), end=ap.Int(-1))
    ap.assert_equal("34", result_string)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
