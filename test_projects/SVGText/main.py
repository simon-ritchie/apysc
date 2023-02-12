"""The test project for the `SVGText` class.

Command examples:
$ python test_projects/SVGText/main.py
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

    ap.SVGText(
        text="Hello, world!",
    )
    ap.SVGText(
        text="x and y coordinates test",
        x=50,
        y=20,
    )
    ap.SVGText(
        text="fill_color test",
        y=40,
        fill_color="#999",
    )
    ap.SVGText(
        text="fill_alpha test",
        y=60,
        fill_color="#999",
        fill_alpha=0.3,
    )
    ap.SVGText(
        text="line_color test",
        y=80,
        line_color="#999",
    )
    ap.SVGText(
        text="line_alpha test",
        y=100,
        line_color="#999",
        line_alpha=0.3,
    )
    ap.SVGText(
        text="line_thickness test",
        y=120,
        line_color="#999",
        line_thickness=2,
    )
    sprite: ap.Sprite = ap.Sprite()
    ap.SVGText(
        text="parent test",
        y=140,
        parent=sprite,
    )
    sprite.x = ap.Number(50)

    svg_text: ap.SVGText = ap.SVGText(
        text="x attribute test",
        y=160,
    )
    svg_text.x = ap.Number(50)

    svg_text = ap.SVGText(
        text="y attribute test",
        y=180,
    )
    svg_text.y = ap.Number(180)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
