"""The test project for the `ForDictValues` class.

Command examples:
$ python test_projects/ForDictValues/main.py
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
    ap.Stage(background_color="#333", stage_width=1000, stage_height=500)

    dict_: ap.Dictionary[str, ap.Number] = ap.Dictionary(
        {"a": ap.Number(100), "b": ap.Number(200)},
    )
    values: ap.Array[ap.Number] = ap.Array([])
    with ap.ForDictValues(dict_=dict_, dict_value_type=ap.Number) as value:
        ap.Rectangle(
            x=value, y=100, width=50, height=50, fill_color="#0af"
        )
        values.append(value)
    values.sort()
    ap.assert_arrays_equal(
        values,
        [100, 200],
    )

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
