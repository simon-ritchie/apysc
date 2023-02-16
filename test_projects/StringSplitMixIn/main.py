"""The test project for the `StringSplitMixIn` class.

Command examples:
$ python test_projects/StringSplitMixIn/main.py
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
        background_color="#333",
        stage_width=1000,
        stage_height=500,
        stage_elem_id="stage",
    )

    string: ap.String = ap.String("100,200,300")
    splitted_strs: ap.Array[ap.String] = string.split(sep=ap.String(","))
    ap.assert_arrays_equal(
        splitted_strs,
        ["100", "200", "300"],
    )

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
