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

    text = ap.MultiLineText(
        text="Hello World!",
        width=100,
        x=50,
        y=250,
        fill_color=ap.Color("#0af"),
        fill_alpha=0.3,
    )
    text.fill_color = ap.Color("#f0a")

    text = ap.MultiLineText(
        text="Bold test 1",
        width=100,
        x=50,
        y=280,
        fill_color=ap.Color("#0af"),
        bold=True,
    )

    text = ap.MultiLineText(
        text="Bold test 2",
        width=100,
        x=50,
        y=310,
        fill_color=ap.Color("#0af"),
    )
    text.bold = ap.True_

    text = ap.MultiLineText(
        text="Italic test 1",
        width=100,
        x=50,
        y=340,
        fill_color=ap.Color("#0af"),
        italic=True,
    )

    text = ap.MultiLineText(
        text="Italic test 2",
        width=100,
        x=50,
        y=370,
        fill_color=ap.Color("#0af"),
    )
    text.italic = ap.True_

    text = ap.MultiLineText(
        text="text-align center test 1. Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit. Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit",
        width=200,
        x=50,
        y=400,
        fill_color=ap.Color("#0af"),
        text_align=ap.CssTextAlign.CENTER,
    )

    text = ap.MultiLineText(
        text="text-align right test. Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit. Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit",
        width=200,
        x=50,
        y=610,
        fill_color=ap.Color("#0af"),
        text_align=ap.CssTextAlign.RIGHT,
    )

    text = ap.MultiLineText(
        text="text-align justify test. Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit. Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit",
        width=200,
        x=300,
        y=30,
        fill_color=ap.Color("#0af"),
        text_align=ap.CssTextAlign.JUSTIFY,
    )

    text = ap.MultiLineText(
        text="text-align center test 2. Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit. Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit",
        width=200,
        x=300,
        y=240,
        fill_color=ap.Color("#0af"),
    )
    text.text_align = ap.CssTextAlign.CENTER

    text = ap.MultiLineText(
        text="text-align right test 1. Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit. Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit",
        width=200,
        x=300,
        y=470,
        fill_color=ap.Color("#0af"),
        text_align=ap.CssTextAlign.JUSTIFY,
        text_align_last=ap.CssTextAlignLast.RIGHT,
    )

    text = ap.MultiLineText(
        text="text-align right test 2. Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit. Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit",
        width=200,
        x=300,
        y=700,
        fill_color=ap.Color("#0af"),
        text_align=ap.CssTextAlign.JUSTIFY,
        text_align_last=ap.CssTextAlignLast.CENTER,
    )

    ap.MultiLineText(
        text="Under line test 1",
        width=200,
        x=550,
        y=30,
        fill_color=ap.Color("#0af"),
        underline=True,
    )

    text = ap.MultiLineText(
        text="Under line test 2",
        width=200,
        x=550,
        y=60,
        fill_color=ap.Color("#0af"),
    )
    text.underline = ap.True_

    text = ap.MultiLineText(
        text="Font size test 1",
        width=300,
        font_size=32,
        x=550,
        y=90,
        fill_color=ap.Color("#0af"),
    )

    text = ap.MultiLineText(
        text="Font size test 2",
        width=300,
        x=550,
        y=130,
        fill_color=ap.Color("#0af"),
    )
    text.font_size = ap.Int(32)

    ap.MultiLineText(
        text="line-height test 1. Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit. Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit",
        width=300,
        x=550,
        y=170,
        fill_color=ap.Color("#0af"),
        line_height=2.0,
    )

    text = ap.MultiLineText(
        text="line-height test 2. Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit. Lorem ipsum dolor sit amet, "
        "consectetur adipiscing elit",
        width=300,
        x=550,
        y=300,
        fill_color=ap.Color("#0af"),
    )
    text.line_height = ap.Number(2.0)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
