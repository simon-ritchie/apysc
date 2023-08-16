"""The test project for the `COLORLESS` constant.

Command examples:
$ python test_projects/COLORLESS/main.py
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

    ap.Rectangle(
        x=50,
        y=50,
        width=50,
        height=50,
        fill_color=ap.COLORLESS,
        line_color=ap.Color("#fff"),
    )

    ap.Rectangle(
        x=150,
        y=50,
        width=50,
        height=50,
        fill_color=ap.Color("#fff"),
        line_color=ap.COLORLESS,
    )

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
