from apysc._material_design.icon.material_power_settings_new_outlined_icon import (
    MaterialPowerSettingsNewOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPowerSettingsNewOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPowerSettingsNewOutlinedIcon = (
            MaterialPowerSettingsNewOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
