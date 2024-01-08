"""The test project for the `MaterialIconBase` class.

Command examples:
$ python test_projects/MaterialIconBase/main.py
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
    # Material Icon: https://fonts.google.com/icons?selected=Material+Icons:search:
    # License: https://www.apache.org/licenses/LICENSE-2.0.html
    svg_path_value: str = "M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"  # noqa
    ap.MaterialIconBase(
        svg_path_value=svg_path_value,
        fill_color=ap.Colors.CYAN_00AAFF,
        fill_alpha=0.5,
        width=24,
        height=24,
        x=20,
        y=20,
    )

    ap.MaterialIconBase(
        svg_path_value=svg_path_value,
        fill_color=ap.Colors.CYAN_00AAFF,
        fill_alpha=ap.Number(0.5),
        width=ap.Int(24),
        height=ap.Int(24),
        x=ap.Number(20),
        y=ap.Number(60),
    )

    ap.MaterialIconBase(
        svg_path_value=svg_path_value,
        fill_color=ap.Colors.CYAN_00AAFF,
        width=30,
        height=30,
        x=20,
        y=100,
    )

    icon: ap.MaterialIconBase = ap.MaterialIconBase(
        svg_path_value=svg_path_value,
        fill_color=ap.Colors.CYAN_00AAFF,
        width=24,
        height=24,
        x=20,
        y=140,
    )
    icon.set_css(name="opacity", value=ap.String("0.2"))

    icon = ap.MaterialIconBase(
        svg_path_value=svg_path_value,
        fill_color=ap.Colors.CYAN_00AAFF,
        width=24,
        height=24,
        x=20,
        y=180,
    )
    icon.scale_x_from_center = ap.Number(1.5)

    icon = ap.MaterialIconBase(
        svg_path_value=svg_path_value,
        fill_color=ap.Colors.CYAN_00AAFF,
        width=24,
        height=24,
        x=20,
        y=220,
    )
    icon.scale_y_from_center = ap.Number(1.5)

    icon = ap.MaterialIconBase(
        svg_path_value=svg_path_value,
        fill_color=ap.Colors.CYAN_00AAFF,
        width=24,
        height=24,
        x=20,
        y=260,
    )
    icon.set_scale_x_from_point(scale_x=ap.Number(2.0), x=ap.Number(20))

    icon = ap.MaterialIconBase(
        svg_path_value=svg_path_value,
        fill_color=ap.Colors.CYAN_00AAFF,
        width=24,
        height=24,
        x=20,
        y=300,
    )
    icon.set_scale_y_from_point(scale_y=ap.Number(2.0), y=ap.Number(300))

    icon = ap.MaterialIconBase(
        svg_path_value=svg_path_value,
        fill_color=ap.Colors.CYAN_00AAFF,
        width=24,
        height=24,
        x=20,
        y=340,
    )
    icon.rotation_around_center = ap.Int(45)

    icon = ap.MaterialIconBase(
        svg_path_value=svg_path_value,
        fill_color=ap.Colors.CYAN_00AAFF,
        width=24,
        height=24,
        x=20,
        y=380,
    )
    icon.set_rotation_around_point(
        rotation=ap.Int(45), x=ap.Number(20), y=ap.Number(380)
    )

    icon = ap.MaterialIconBase(
        svg_path_value=svg_path_value,
        fill_color=ap.Colors.CYAN_00AAFF,
        width=24,
        height=24,
        x=20,
        y=420,
    )
    icon.flip_x = ap.True_

    icon = ap.MaterialIconBase(
        svg_path_value=svg_path_value,
        fill_color=ap.Colors.CYAN_00AAFF,
        width=24,
        height=24,
        x=20,
        y=460,
    )
    icon.flip_y = ap.True_

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
