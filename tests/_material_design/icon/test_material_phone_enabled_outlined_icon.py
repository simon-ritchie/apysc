from apysc._material_design.icon.material_phone_enabled_outlined_icon import (
    MaterialPhoneEnabledOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPhoneEnabledOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPhoneEnabledOutlinedIcon = MaterialPhoneEnabledOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
