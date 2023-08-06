"""The test project for the WeekdayMixIn class.

Command examples:
$ python test_projects/WeekdayMixIn/main.py
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
        background_color=ap.Color("#333"),
        stage_width=1000,
        stage_height=500,
        stage_elem_id="stage",
    )
    datetime_: ap.DateTime = ap.DateTime(year=2022, month=11, day=27)
    weekday_js: ap.Int = datetime_.weekday_js
    ap.assert_equal(weekday_js, 0)

    datetime_ = ap.DateTime(year=2022, month=11, day=28)
    weekday_js = datetime_.weekday_js
    ap.assert_equal(weekday_js, 1)

    datetime_ = ap.DateTime(year=2022, month=11, day=26)
    weekday_js = datetime_.weekday_js
    ap.assert_equal(weekday_js, 6)

    datetime_ = ap.DateTime(year=2022, month=11, day=21)
    weekday_py: ap.Int = datetime_.weekday_py
    ap.assert_equal(weekday_py, 0)

    datetime_ = ap.DateTime(year=2022, month=11, day=22)
    weekday_py = datetime_.weekday_py
    ap.assert_equal(weekday_py, 1)

    datetime_ = ap.DateTime(year=2022, month=11, day=27)
    weekday_py = datetime_.weekday_py
    ap.assert_equal(weekday_py, 6)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == "__main__":
    main()
