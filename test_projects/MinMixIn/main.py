"""The test project for the `MinMixIn` class.

Command examples:
$ python test_projects/MinMixIn/main.py
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
    _: ap.Stage = ap.Stage(background_color="#333")

    result: ap.Number = ap.Math.min(
        values=ap.Array([10, ap.Int(9), ap.Number(9.5), 10.5])
    )
    ap.assert_equal(result, 9)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
