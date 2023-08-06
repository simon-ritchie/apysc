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
        background_color=ap.Color("#333"),
        stage_width=1200,
        stage_height=900,
    )
    ap.set_debug_mode()

    triangle_1: ap.Triangle = ap.Triangle(
        x1=75,
        y1=50,
        x2=50,
        y2=100,
        x3=100,
        y3=100,
        fill_color=ap.Color("#0af"),
        fill_alpha=0.5,
    )
    triangle_1.click(handler=on_triangle_1_click_1)
    triangle_1.click(handler=on_triangle_1_click_2)

    triangle_2: ap.Triangle = ap.Triangle(
        x1=175,
        y1=50,
        x2=150,
        y2=100,
        x3=200,
        y3=100,
        fill_color=ap.Color("#f0a"),
        line_color=ap.Color("#fff"),
        line_thickness=3,
        line_alpha=0.5,
    )
    triangle_2.click(handler=on_triangle_2_click_1)

    triangle_3: ap.Triangle = ap.Triangle(
        x1=275,
        y1=50,
        x2=250,
        y2=100,
        x3=300,
        y3=100,
        fill_color=ap.Color("#f0a"),
    )
    triangle_3.click(handler=on_triangle_3_click_1)

    triangle_4: ap.Triangle = ap.Triangle(
        x1=375,
        y1=50,
        x2=350,
        y2=100,
        x3=400,
        y3=100,
        fill_color=ap.Color("#f0a"),
    )
    triangle_4.click(handler=on_triangle_4_click_1)

    triangle_5: ap.Triangle = ap.Triangle(
        x1=475,
        y1=50,
        x2=450,
        y2=100,
        x3=500,
        y3=100,
        fill_color=ap.Color("#f0a"),
    )
    triangle_5.click(handler=on_triangle_5_click_1)

    triangle_6: ap.Triangle = ap.Triangle(
        x1=575,
        y1=50,
        x2=550,
        y2=100,
        x3=600,
        y3=100,
        fill_color=ap.Color("#f0a"),
    )
    triangle_6.click(handler=on_triangle_6_click_1)

    triangle_7: ap.Triangle = ap.Triangle(
        x1=675,
        y1=50,
        x2=650,
        y2=100,
        x3=700,
        y3=100,
        fill_color=ap.Color("#f0a"),
    )
    triangle_7.click(handler=on_triangle_7_click_1)

    triangle_8: ap.Triangle = ap.Triangle(
        x1=775,
        y1=50,
        x2=750,
        y2=100,
        x3=800,
        y3=100,
        fill_color=ap.Color("#f0a"),
    )
    triangle_8.click(handler=on_triangle_8_click_1)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def on_triangle_1_click_1(e: ap.MouseEvent[ap.Triangle], options: dict) -> None:
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


def on_triangle_1_click_2(e: ap.MouseEvent[ap.Triangle], options: dict) -> None:
    """
    The handler for the click event.

    Parameters
    ----------
    e : ap.MouseEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    e.this.x1 += -1
    ap.trace(e.this._points)


def on_triangle_2_click_1(e: ap.MouseEvent[ap.Triangle], options: dict) -> None:
    """
    The handler for the click event.

    Parameters
    ----------
    e : ap.MouseEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    e.this.x1 += 1
    e.this.y1 += 1


def on_triangle_3_click_1(e: ap.MouseEvent[ap.Triangle], options: dict) -> None:
    """
    The handler for the click event.

    Parameters
    ----------
    e : ap.MouseEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    e.this.x2 += 1


def on_triangle_4_click_1(e: ap.MouseEvent[ap.Triangle], options: dict) -> None:
    """
    The handler for the click event.

    Parameters
    ----------
    e : ap.MouseEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    e.this.y2 += 1


def on_triangle_5_click_1(e: ap.MouseEvent[ap.Triangle], options: dict) -> None:
    """
    The handler for the click event.

    Parameters
    ----------
    e : ap.MouseEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    e.this.x2 += 1
    e.this.y2 += 1


def on_triangle_6_click_1(e: ap.MouseEvent[ap.Triangle], options: dict) -> None:
    """
    The handler for the click event.

    Parameters
    ----------
    e : ap.MouseEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    e.this.x3 += 1


def on_triangle_7_click_1(e: ap.MouseEvent[ap.Triangle], options: dict) -> None:
    """
    The handler for the click event.

    Parameters
    ----------
    e : ap.MouseEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    e.this.y3 += 1


def on_triangle_8_click_1(e: ap.MouseEvent[ap.Triangle], options: dict) -> None:
    """
    The handler for the click event.

    Parameters
    ----------
    e : ap.MouseEvent[ap.Triangle]
        Event instance.
    options : dict
        Optional argument dictionary.
    """
    e.this.x3 += 1
    e.this.y3 += 1


if __name__ == "__main__":
    main()
