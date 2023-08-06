"""The test project for the `ToFixedMixIn` class.

Command examples:
$ python test_projects/ToFixedMixIn/main.py
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

    num: ap.Number = ap.Number(10.789)
    fixed_float_str: ap.String = num.to_fixed(digits=2)
    ap.assert_equal(fixed_float_str, "10.79")

    fixed_float_str = num.to_fixed(digits=5)
    ap.assert_equal(fixed_float_str, "10.78900")

    fixed_float_str = num.to_fixed(digits=0)
    ap.assert_equal(fixed_float_str, "11")

    digits: ap.Int = ap.Int(1)
    fixed_float_str = num.to_fixed(digits=digits)
    ap.assert_equal(fixed_float_str, "10.8")

    int_val: ap.Int = ap.Int(10)
    fixed_float_str = int_val.to_fixed(digits=2)
    ap.assert_equal(fixed_float_str, "10.00")

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == "__main__":
    main()
