from apysc._material_design.icon.material_settings_overscan_outlined_icon import (
    MaterialSettingsOverscanOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsOverscanOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsOverscanOutlinedIcon = (
            MaterialSettingsOverscanOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
