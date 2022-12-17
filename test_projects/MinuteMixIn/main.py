"""A test project for the MinuteMixIn class.

Command examples:
$ python test_projects/MinuteMixIn/main.py
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
    datetime_: ap.DateTime = ap.DateTime(
        year=2022, month=11, day=26, hour=10, minute=30
    )
    minute: ap.Int = datetime_.minute
    ap.assert_equal(minute, 30)

    minute.value = 50
    datetime_.minute = minute
    ap.assert_equal(datetime_.minute, 50)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == "__main__":
    main()
