from apysc._material_design.icon.material_settings_overscan_icon import (
    MaterialSettingsOverscanIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsOverscanIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsOverscanIcon = MaterialSettingsOverscanIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
