"""The test project for the `SvgMask` class.

Command examples:
$ python test_projects/SvgMask/main.py
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
    ap.Stage(background_color=ap.Color("#333"), stage_width=1000, stage_height=760)

    mask_1: ap.SvgMask = ap.SvgMask()
    circle_1: ap.Circle = ap.Circle(x=150, y=100, radius=50)
    mask_1.add_svg_masking_object(masking_object=circle_1)
    rectangle_1: ap.Rectangle = ap.Rectangle(
        x=50, y=50, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
    )
    rectangle_1.svg_mask = mask_1

    mask_2: ap.SvgMask = ap.SvgMask()
    circle_2: ap.Circle = ap.Circle(x=300, y=100, radius=50)
    mask_2.add_svg_masking_object(masking_object=circle_2, alpha=0.5)
    rectangle_2: ap.Rectangle = ap.Rectangle(
        x=200, y=50, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
    )
    rectangle_2.svg_mask = mask_2

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
