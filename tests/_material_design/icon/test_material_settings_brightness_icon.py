from apysc._material_design.icon.material_settings_brightness_icon import (
    MaterialsettingsBrightnessIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsBrightnessIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsBrightnessIcon = MaterialsettingsBrightnessIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
