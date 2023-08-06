"""The test project for the `range` function.

Command examples:
$ python test_projects/range/main.py
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

    range_arr: ap.Array[ap.Int] = ap.range(5)
    ap.assert_equal(range_arr, [0, 1, 2, 3, 4])

    range_arr = ap.range(2, 5)
    ap.assert_equal(range_arr, [2, 3, 4])

    range_arr = ap.range(2, 10, 2)
    ap.assert_equal(range_arr, [2, 4, 6, 8])

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
