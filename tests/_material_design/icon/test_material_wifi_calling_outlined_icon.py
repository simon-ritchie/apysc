from apysc._material_design.icon.material_wifi_calling_outlined_icon import (
    MaterialWifiCallingOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialWifiCallingOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialWifiCallingOutlinedIcon = MaterialWifiCallingOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
