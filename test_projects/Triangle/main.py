"""The test project for the `Triangle` class.

Command examples:
$ python test_projects/Triangle/main.py
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

    triangle_1: ap.Triangle = ap.Triangle(
        x1=75,
        y1=50,
        x2=50,
        y2=100,
        x3=100,
        y3=100,
        fill_color="#0af",
        fill_alpha=0.5,
    )
    triangle_1.click(handler=on_triangle_1_click)

    ap.Triangle(
        x1=175,
        y1=50,
        x2=150,
        y2=100,
        x3=200,
        y3=100,
        line_color="#fff",
        line_thickness=3,
        line_alpha=0.5,
    )

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH)


def on_triangle_1_click(e: ap.MouseEvent[ap.Triangle], options: dict) -> None:
    """
    The handler for the click event.

    Parameters
    ----------
    e : ap.MouseEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    e.this.fill_color = ap.String("#f0a")


if __name__ == "__main__":
    main()
