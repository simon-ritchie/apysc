"""The test project for the `MaterialSettingsUtils` class.

Command examples:
$ python test_projects/MaterialSettingsUtils/main.py
"""

import sys

sys.path.append("./")

import os
from types import ModuleType

import env_var_util

env_var_util.apply_material_icons_import_skipping_setting()

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

    primary_color: ap.Color = ap.MaterialSettingsUtils.get_primary_color(
        argument_color=ap.Colors.BLUE_0000FF,
    )
    ap.assert_equal(primary_color, ap.Colors.BLUE_0000FF)

    primary_color = ap.MaterialSettingsUtils.get_primary_color(
        argument_color=None,
    )
    ap.assert_equal(primary_color, ap.MaterialSettingsUtils._fixed_color_scheme.primary)

    light_color_scheme: ap.MaterialColorScheme = ap.MaterialColorScheme(
        primary=ap.Colors.ACID_GREEN_B0BF1A,
        on_primary=ap.Colors.ALGAE_GREEN_64E986,
        secondary=ap.Colors.ALICE_BLUE_F0F8FF,
        on_secondary=ap.Colors.ALIEN_GRAY_736F6E,
        error=ap.Colors.ALOE_VERA_GREEN_98F516,
        on_error=ap.Colors.ANTIQUE_WHITE_FAEBD7,
        surface=ap.Colors.AQUAMARINE_STONE_348781,
        on_surface=ap.Colors.AQUAMARINE_7FFFD4,
        primary_container=ap.Colors.ARMY_BROWN_827B60,
        on_primary_container=ap.Colors.AZTECH_PURPLE_893BFF,
        secondary_container=ap.Colors.ASH_GRAY_666362,
        on_secondary_container=ap.Colors.AZURE_BLUE_4863A0,
        tertiary=ap.Colors.AVOCADO_GREEN_B2C248,
        on_tertiary=ap.Colors.BABY_PINK_FAAFBA,
        error_container=ap.Colors.BALLOON_BLUE_2B60DE,
        on_error_container=ap.Colors.BAKERS_BROWN_5C3317,
        outline=ap.Colors.BASIL_GREEN_829F82,
        outline_variant=ap.Colors.BANANA_YELLOW_F5E216,
    )
    ap.MaterialSettings.set_light_color_scheme(color_scheme=light_color_scheme)
    dark_color_scheme: ap.MaterialColorScheme = ap.MaterialColorScheme(
        primary=ap.Colors.DARK_MOCCASIN_827839,
        on_primary=ap.Colors.KHAKI_GREEN_8A865D,
        secondary=ap.Colors.MILLENNIUM_JADE_93917C,
        on_secondary=ap.Colors.DARK_BEIGE_9F8C76,
        error=ap.Colors.BULLET_SHELL_AF9B60,
        on_error=ap.Colors.SANDSTONE_786D5F,
        surface=ap.Colors.TAUPE_483C32,
        on_surface=ap.Colors.MOCHA_493D26,
        primary_container=ap.Colors.MILK_CHOCOLATE_513B1C,
        on_primary_container=ap.Colors.GRAY_BROWN_3D3635,
        secondary_container=ap.Colors.DARK_COFFEE_3B2F2F,
        on_secondary_container=ap.Colors.WESTERN_CHARCOAL_49413F,
        tertiary=ap.Colors.OLD_BURGUNDY_43302E,
        on_tertiary=ap.Colors.RED_BROWN_622F22,
        error_container=ap.Colors.DARK_BROWN_654321,
        on_error_container=ap.Colors.SEPIA_BROWN_704214,
        outline=ap.Colors.DARK_BRONZE_804A00,
        outline_variant=ap.Colors.COFFEE_6F4E37,
    )
    ap.MaterialSettings.set_dark_color_scheme(color_scheme=dark_color_scheme)

    ap.MaterialSettings.switch_to_light_color_scheme()
    primary_color = ap.MaterialSettingsUtils.get_primary_color(
        argument_color=None,
    )
    ap.assert_equal(primary_color, light_color_scheme.primary)

    ap.MaterialSettings.switch_to_dark_color_scheme()
    primary_color = ap.MaterialSettingsUtils.get_primary_color(
        argument_color=None,
    )
    ap.assert_equal(primary_color, dark_color_scheme.primary)

    ap.save_overall_html(dest_dir_path=_DEST_DIR_PATH, minify=False)


if __name__ == "__main__":
    main()
