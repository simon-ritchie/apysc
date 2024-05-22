from apysc._material_design.icon.material_wifi_protected_setup_outlined_icon import (
    MaterialWifiProtectedSetupOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialWifiProtectedSetupOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialWifiProtectedSetupOutlinedIcon = (
            MaterialWifiProtectedSetupOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
