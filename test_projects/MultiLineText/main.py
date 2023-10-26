"""The test project for the `MultiLineText` class.

Command examples:
$ python test_projects/MultiLineText/main.py
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
    ap.MultiLineText(text="<font color='red'>Hello World!</>", width=100)

    ap.MultiLineText(
        text="<font color='red'>Hello World!</>",
        width=100,
        x=100,
        y=30,
    )

    ap.MultiLineText(
        text="Hello World!",
        width=100,
        x=50,
        y=60,
        fill_color=ap.Color("#0af"),
    )

    text: ap.MultiLineText = ap.MultiLineText(
        text="Hello World!",
        width=100,
        x=50,
        y=90,
        fill_color=ap.Color("#0af"),
    )
    text.fill_color = ap.Color("#f0a")

    ap.MultiLineText(
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        width=150,
        x=50,
        y=110,
        fill_color=ap.Color("#0af"),
    )

    text: ap.MultiLineText = ap.MultiLineText(
        text="Hello World!",
        width=100,
        x=50,
        y=250,
        fill_color=ap.Color("#0af"),
        fill_alpha=0.3,
    )
    text.fill_color = ap.Color("#f0a")

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
