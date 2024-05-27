"""The test project for the `ClampMixIn`.

Command examples:
$ python test_projects/ClampMixIn/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

import apysc as ap
from apysc._file import file_util
import importlib

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

    result_1: ap.Number = ap.Math.clamp(
        value=ap.Number(5.5), min_=ap.Number(10.5), max_=ap.Number(20.5)
    )
    ap.assert_equal(result_1, ap.Number(10.5))

    result_1 = ap.Math.clamp(
        value=ap.Number(15.5), min_=ap.Number(10.5), max_=ap.Number(20.5)
    )
    ap.assert_equal(result_1, ap.Number(15.5))

    result_1 = ap.Math.clamp(
        value=ap.Number(21.5), min_=ap.Number(10.5), max_=ap.Number(20.5)
    )
    ap.assert_equal(result_1, ap.Number(20.5))

    result_2: ap.Int = ap.Math.clamp(
        value=ap.Int(5), min_=ap.Int(10), max_=ap.Int(20)
    )
    ap.assert_equal(result_2, ap.Int(10))

    result_2 = ap.Math.clamp(
        value=ap.Int(15), min_=ap.Int(10), max_=ap.Int(20)
    )
    ap.assert_equal(result_2, ap.Int(15))

    result_2 = ap.Math.clamp(
        value=ap.Int(21), min_=ap.Int(10), max_=ap.Int(20)
    )
    ap.assert_equal(result_2, ap.Int(20))

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
