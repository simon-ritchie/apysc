"""The test project for the VariableNameSuffixInterface class.

Command examples:
$ python test_projects/VariableNameSuffixInterface/main.py
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

    int_1: ap.Int = ap.Int(10, variable_name_suffix="test_int_1")
    int_1 += 10
    ap.trace(int_1)

    circle: ap.Circle = ap.Circle(
        x=100, y=100, radius=50, fill_color="#0af", variable_name_suffix="test_circle"
    )
    circle.x = ap.Int(150)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
