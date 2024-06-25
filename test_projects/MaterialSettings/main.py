"""The test project for the `MaterialSettings` class.

Command examples:
$ python test_projects/MaterialSettings/main.py
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

    ap.assert_true(ap.MaterialSettings.current_color_scheme_is_light_color_scheme())
    ap.assert_false(ap.MaterialSettings.current_color_scheme_is_dark_color_scheme())

    ap.MaterialSettings.switch_to_dark_color_scheme()
    ap.assert_false(ap.MaterialSettings.current_color_scheme_is_light_color_scheme())
    ap.assert_true(ap.MaterialSettings.current_color_scheme_is_dark_color_scheme())

    ap.MaterialSettings.switch_to_light_color_scheme()
    ap.assert_true(ap.MaterialSettings.current_color_scheme_is_light_color_scheme())
    ap.assert_false(ap.MaterialSettings.current_color_scheme_is_dark_color_scheme())

    light_color_scheme_rectangle: ap.Rectangle = ap.Rectangle(
        x=50,
        y=50,
        width=50,
        height=50,
        fill_color=ap.Colors.GRAY_CCCCCC,
    )
    light_color_scheme_rectangle.click(handler=_on_light_scheme_rectangle_click)

    dark_color_scheme_rectangle: ap.Rectangle = ap.Rectangle(
        x=150,
        y=50,
        width=50,
        height=50,
        fill_color=ap.Colors.GRAY_999999,
    )
    dark_color_scheme_rectangle.click(handler=_on_dark_scheme_rectangle_click)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


def _on_light_scheme_rectangle_click(
    e: ap.MouseEvent[ap.Rectangle], options: dict
) -> None:
    """
    The handler that called when the `light_color_scheme_rectangle` is clicked.

    Parameters
    ----------
    e : MouseEvent
        Created MouseEvent instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.MaterialSettings.switch_to_light_color_scheme()
    ap.assert_true(ap.MaterialSettings.current_color_scheme_is_light_color_scheme())
    ap.assert_false(ap.MaterialSettings.current_color_scheme_is_dark_color_scheme())


def _on_dark_scheme_rectangle_click(
    e: ap.MouseEvent[ap.Rectangle], options: dict
) -> None:
    """
    The handler that called when the `dark_color_scheme_rectangle` is clicked.

    Parameters
    ----------
    e : MouseEvent
        Created MouseEvent instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.MaterialSettings.switch_to_dark_color_scheme()
    ap.assert_false(ap.MaterialSettings.current_color_scheme_is_light_color_scheme())
    ap.assert_true(ap.MaterialSettings.current_color_scheme_is_dark_color_scheme())


if __name__ == "__main__":
    main()
