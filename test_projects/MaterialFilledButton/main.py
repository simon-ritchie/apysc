"""The test project for the `MaterialFilledButton` class.

Command examples:
$ python test_projects/MaterialFilledButton/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

import env_var_util

env_var_util.apply_material_icons_import_skipping_setting()

import apysc as ap
from apysc._file import file_util
from apysc._material_design.icon.material_home_icon import MaterialHomeIcon
from apysc._material_design.icon.material_create_icon import MaterialCreateIcon

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

    button_1: ap.MaterialFilledButton = ap.MaterialFilledButton(
        label="Filled button 1",
    )
    button_1.x = ap.Number(20)
    button_1.y = ap.Number(20)

    button_2: ap.MaterialFilledButton = ap.MaterialFilledButton(
        label="Filled button 2",
        prefix_icon=MaterialHomeIcon(),
    )
    button_2.x = ap.Number(20)
    button_2.y = ap.Number(80)

    button_3: ap.MaterialFilledButton = ap.MaterialFilledButton(
        label="Filled button 3",
        suffix_icon=MaterialHomeIcon(),
    )
    button_3.x = ap.Number(20)
    button_3.y = ap.Number(140)

    button_4: ap.MaterialFilledButton = ap.MaterialFilledButton(
        label="Filled button 4",
        prefix_icon=MaterialHomeIcon(),
        suffix_icon=MaterialCreateIcon(),
    )
    button_4.x = ap.Number(20)
    button_4.y = ap.Number(200)

    ap.MaterialFilledButton = ap.MaterialFilledButton(
        label="Filled button 5",
        prefix_icon=MaterialHomeIcon(),
        x=20,
        y=260,
    )

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
