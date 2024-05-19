from apysc._material_design.icon.material_vpn_key_outlined_icon import (
    MaterialvpnKeyOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvpnKeyOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvpnKeyOutlinedIcon = MaterialvpnKeyOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
