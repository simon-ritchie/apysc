from apysc._material_design.icon.material_settings_brightness_outlined_icon import (
    MaterialsettingsBrightnessOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsBrightnessOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsBrightnessOutlinedIcon = (
            MaterialsettingsBrightnessOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
