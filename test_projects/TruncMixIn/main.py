"""The test project for the `TruncMixIn` class.

Command examples:
$ python test_projects/TruncMixIn/main.py
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
    _: ap.Stage = ap.Stage(background_color=ap.Color("#333"))

    result: ap.Int = ap.Math.trunc(ap.Int(10))
    ap.assert_equal(result, 10)

    result = ap.Math.trunc(ap.Number(10.5))
    ap.assert_equal(result, 10)

    result = ap.Math.trunc(ap.Boolean(True))
    ap.assert_equal(result, 1)

    result = ap.Math.trunc(ap.Boolean(False))
    ap.assert_equal(result, 0)

    result = ap.Math.trunc(ap.String("10.5"))
    ap.assert_equal(result, 10)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
