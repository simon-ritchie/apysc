"""The test project for the `MaxMixIn` class.

Command examples:
$ python test_projects/MaxMixIn/main.py
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

    result: ap.Number = ap.Math.max(
        values=ap.Array([10, ap.Int(11), ap.Number(9.5), 10.5])
    )
    ap.assert_equal(result, 11)
    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
