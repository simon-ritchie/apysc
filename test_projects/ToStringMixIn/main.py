"""Test project for `ToStringMixIn` class.

Command examples:
$ python test_projects/ToStringMixIn/main.py
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
    ap.Stage(
        background_color=ap.Color("#333"),
        stage_width=1000,
        stage_height=1000,
        stage_elem_id="stage",
    )
    int_1: ap.Int = ap.Int(10)
    string_1: ap.String = int_1.to_string()
    ap.assert_equal(string_1, "10")

    number_1: ap.Number = ap.Number(10.5)
    string_2: ap.String = number_1.to_string()
    ap.assert_equal(string_2, "10.5")

    arr_1: ap.Array = ap.Array([1, 2, 3])
    string_3: ap.String = arr_1.to_string()
    ap.assert_equal(string_3, "1,2,3")

    bool_1: ap.Boolean = ap.Boolean(True)
    string_4: ap.String = bool_1.to_string()
    ap.assert_equal(string_4, "true")

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
