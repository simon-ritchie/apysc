from apysc._material_design.icon.material_phone_enabled_outlined_icon import MaterialphoneEnabledOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialphoneEnabledOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialphoneEnabledOutlinedIcon = MaterialphoneEnabledOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
