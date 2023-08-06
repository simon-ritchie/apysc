"""The test project for the `assert_greater_equal` interface.

Command examples:
$ python test_projects/assert_greater_equal/main.py
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

    ap.assert_greater_equal(left=10, right=10)
    ap.assert_greater_equal(left=10, right=9)
    ap.assert_greater_equal(left=ap.Int(10), right=10)
    ap.assert_greater_equal(left=ap.Int(10), right=9)
    ap.assert_greater_equal(left=10, right=ap.Int(10))
    ap.assert_greater_equal(left=10, right=ap.Int(9))

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


if __name__ == "__main__":
    main()
