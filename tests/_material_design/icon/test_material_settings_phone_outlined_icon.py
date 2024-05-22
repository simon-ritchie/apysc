from apysc._material_design.icon.material_settings_phone_outlined_icon import (
    MaterialSettingsPhoneOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsPhoneOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsPhoneOutlinedIcon = MaterialSettingsPhoneOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
