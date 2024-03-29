"""The test project for the `ForArrayValues` class.

Command examples:
$ python test_projects/ForArrayValues/main.py
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
    ap.Stage(background_color=ap.Color("#333"), stage_width=1000, stage_height=500)

    arr: ap.Array[ap.Number] = ap.Array([ap.Number(50), ap.Number(150), ap.Number(250)])
    values: ap.Array[ap.Number] = ap.Array([])
    with ap.ForArrayValues(arr=arr, arr_value_type=ap.Number) as value:
        values.append(value)
        ap.Circle(x=value, y=150, radius=20, fill_color=ap.Color("#0af"))

    ap.assert_arrays_equal(
        values,
        [50, 150, 250],
    )
    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
