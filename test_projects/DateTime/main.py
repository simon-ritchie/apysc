"""The test project for the DateTime class.

Command examples:
$ python test_projects/DateTime/main.py
"""

import sys
from datetime import datetime

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
    now: datetime = datetime.now()
    datetime_: ap.DateTime = ap.DateTime.now()
    ap.assert_equal(datetime_.year, now.year)
    ap.assert_equal(datetime_.month, now.month)
    ap.assert_equal(datetime_.day, now.day)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == "__main__":
    main()
