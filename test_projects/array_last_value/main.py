"""Test project for the `Array` class `last_value` property.

Command examples:
$ python test_projects/array_last_value/main.py
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

    arr_1: ap.Array[ap.Int] = ap.Array([], fixed_value_type=ap.Int)
    last_value_1: ap.Int = arr_1.last_value
    ap.assert_undefined(last_value_1)

    arr_1.append(ap.Int(10))
    last_value_1 = arr_1.last_value
    ap.assert_equal(last_value_1, 10)

    arr_1.append(ap.Int(20))
    last_value_1 = arr_1.last_value
    ap.assert_equal(last_value_1, 20)

    arr_1 = ap.Array([ap.Int(10), ap.Int(20), ap.Int(30)])
    last_value_1 = arr_1.last_value
    ap.assert_equal(last_value_1, 30)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
