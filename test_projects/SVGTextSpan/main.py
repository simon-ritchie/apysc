"""The test project for the `SVGTextSpan` class.

Command examples:
$ python test_projects/SVGTextSpan/main.py
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
    ap.Stage(
        background_color="#333",
        stage_width=1000,
        stage_height=1000,
        stage_elem_id="stage",
    )

    _: ap.SVGText = ap.SVGText.create_with_svg_text_spans(
        text_spans=[
            ap.SVGTextSpan(text="SVGTextSpan test 1 "),
            ap.SVGTextSpan(
                text="SVGTextSpan test 2 ",
                font_size=16,
                fill_color="#aaa",
                font_family=["Arial"],
            ),
            ap.SVGTextSpan(text="SVGTextSpan test 3"),
        ],
        font_size=12,
        font_family=["Impact"],
        x=50,
        y=50,
        fill_color="#0af",
    )

    _ = ap.SVGText.create_with_svg_text_spans(
        text_spans=[
            ap.SVGTextSpan(text="fill_alpha test 1 "),
            ap.SVGTextSpan(
                text="fill_alpha test 2 ",
                fill_alpha=1.0,
            ),
            ap.SVGTextSpan(
                text="fill_alpha test 3",
                fill_alpha=0.2,
            ),
        ],
        x=50,
        y=80,
        fill_color="#0af",
        fill_alpha=0.5,
    )

    _ = ap.SVGText.create_with_svg_text_spans(
        text_spans=[
            ap.SVGTextSpan(text="line_color test 1 "),
            ap.SVGTextSpan(
                text="line_color test 2 ",
                line_color="#666",
            ),
            ap.SVGTextSpan(
                text="line_color test 3",
            ),
        ],
        x=50,
        y=110,
        fill_color="",
        line_color="#0af",
    )

    _ = ap.SVGText.create_with_svg_text_spans(
        text_spans=[
            ap.SVGTextSpan(text="line_alpha test 1 "),
            ap.SVGTextSpan(
                text="line_alpha test 2 ",
                line_alpha=0.2,
            ),
            ap.SVGTextSpan(
                text="line_alpha test 3",
            ),
        ],
        x=50,
        y=130,
        fill_color="",
        line_color="#0af",
        line_alpha=0.5,
    )

    _ = ap.SVGText.create_with_svg_text_spans(
        text_spans=[
            ap.SVGTextSpan(text="line_thickness test 1 "),
            ap.SVGTextSpan(
                text="line_thickness test 2 ",
                line_thickness=1,
            ),
            ap.SVGTextSpan(
                text="line_thickness test 3",
            ),
        ],
        x=50,
        y=150,
        fill_color="",
        line_color="#0af",
        line_thickness=3,
    )

    _ = ap.SVGText.create_with_svg_text_spans(
        text_spans=[
            ap.SVGTextSpan(text="bold test 1 "),
            ap.SVGTextSpan(
                text="bold test 2 ",
                bold=False,
            ),
            ap.SVGTextSpan(
                text="bold test 3",
            ),
        ],
        x=50,
        y=170,
        fill_color="#aaa",
        bold=True,
    )

    _ = ap.SVGText.create_with_svg_text_spans(
        text_spans=[
            ap.SVGTextSpan(text="italic test 1 "),
            ap.SVGTextSpan(
                text="italic test 2 ",
                italic=False,
            ),
            ap.SVGTextSpan(
                text="italic test 3",
            ),
        ],
        x=50,
        y=190,
        fill_color="#aaa",
        italic=True,
    )

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
