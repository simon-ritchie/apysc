"""The test project for the `True_` constant.

Command examples:
$ python test_projects/True_/main.py
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
        background_color="#333",
        stage_width=1200,
        stage_height=900,
    )

    ap.assert_true(ap.True_)
    ap.assert_true(ap.True_ == ap.Boolean(True))
    ap.assert_true(ap.True_)
    ap.assert_false(ap.True_ == ap.Boolean(False))
    ap.assert_false(not ap.True_)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
