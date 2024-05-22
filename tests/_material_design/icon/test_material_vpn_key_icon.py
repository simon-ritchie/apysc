from apysc._material_design.icon.material_vpn_key_icon import MaterialVpnKeyIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVpnKeyIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVpnKeyIcon = MaterialVpnKeyIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
