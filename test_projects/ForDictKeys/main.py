"""The test project for the `ForDictKeys` class.

Command examples:
$ python test_projects/ForDictKeys/main.py
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

    dict_: ap.Dictionary[ap.String, int] = ap.Dictionary(
        {
            ap.String("apple"): 120,
            ap.String("orange"): 200,
        }
    )
    keys: ap.Array[ap.String] = ap.Array([])
    with ap.ForDictKeys(dict_=dict_, dict_key_type=ap.String) as key:
        keys.append(key)
    ap.assert_arrays_equal(
        keys,
        ["apple", "orange"],
    )
    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
