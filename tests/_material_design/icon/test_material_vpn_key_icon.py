from apysc._material_design.icon.material_vpn_key_icon import MaterialvpnKeyIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvpnKeyIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvpnKeyIcon = MaterialvpnKeyIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
