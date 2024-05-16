"""The test project for the `SvgIcon` class.

Command examples:
$ python test_projects/SvgIcon/main.py
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

    # Material Icons
    # https://fonts.google.com/icons?selected=Material+Icons:search:
    # APACHE LICENSE, VERSION 2.0
    # https://www.apache.org/licenses/LICENSE-2.0.html
    SVG_ICON_HTML: str = (
        '<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="#000000"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M23 11.01L18 11c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5c.55 0 1-.45 1-1v-9c0-.55-.45-.99-1-.99zM23 20h-5v-7h5v7zM20 2H2C.89 2 0 2.89 0 4v12c0 1.1.89 2 2 2h7v2H7v2h8v-2h-2v-2h2v-2H2V4h18v5h2V4c0-1.11-.9-2-2-2zm-8.03 7L11 6l-.97 3H7l2.47 1.76-.94 2.91 2.47-1.8 2.47 1.8-.94-2.91L15 9h-3.03z"/></svg>'  # noqa
    )

    ap.SvgIcon(
        svg_icon_html=SVG_ICON_HTML,
    )

    ap.SvgIcon(
        svg_icon_html=SVG_ICON_HTML,
        x=25,
        y=50,
    )

    svg_icon: ap.SvgIcon = ap.SvgIcon(
        svg_icon_html=SVG_ICON_HTML,
    )
    svg_icon.x = ap.Number(50)
    svg_icon.y = ap.Number(75)

    ap.SvgIcon(
        svg_icon_html=SVG_ICON_HTML,
        x=25,
        y=100,
        fill_color=ap.Colors.CYAN_00AAFF,
    )

    svg_icon = ap.SvgIcon(
        svg_icon_html=SVG_ICON_HTML,
        x=25,
        y=125,
    )
    svg_icon.fill_color = ap.Colors.MAGENTA_FF00FF

    ap.SvgIcon(
        svg_icon_html=SVG_ICON_HTML,
        x=25,
        y=150,
        fill_color=ap.Colors.CYAN_00AAFF,
        fill_alpha=0.5,
    )

    svg_icon = ap.SvgIcon(
        svg_icon_html=SVG_ICON_HTML,
        x=25,
        y=175,
    )
    svg_icon.fill_alpha = ap.Number(0.5)

    svg_icon = ap.SvgIcon(
        svg_icon_html=SVG_ICON_HTML,
        x=25,
        y=200,
        size=36,
        fill_color=ap.Colors.CYAN_00AAFF,
    )

    sprite: ap.Sprite = ap.Sprite()
    sprite.x = ap.Number(25)
    sprite.y = ap.Number(250)
    ap.SvgIcon(
        svg_icon_html=SVG_ICON_HTML,
        parent=sprite,
    )

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
