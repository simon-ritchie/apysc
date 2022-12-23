"""The test project for the DaysMixIn class.

Command examples:
$ python test_projects/DaysMixIn/main.py
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
    datetime_1: ap.DateTime = ap.DateTime(year=2022, month=12, day=23)
    datetime_2: ap.DateTime = ap.DateTime(year=2022, month=12, day=21)
    timedelta_: ap.TimeDelta = datetime_1 - datetime_2
    ap.assert_equal(timedelta_.days, 2)

    datetime_3: ap.DateTime = ap.DateTime(year=2022, month=12, day=23)
    datetime_4: ap.DateTime = ap.DateTime(year=2022, month=12, day=21, millisecond=1)
    timedelta_ = datetime_3 - datetime_4
    ap.assert_equal(timedelta_.days, 1)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == "__main__":
    main()
