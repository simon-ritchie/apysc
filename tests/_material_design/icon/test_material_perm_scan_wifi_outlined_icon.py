from apysc._material_design.icon.material_perm_scan_wifi_outlined_icon import (
    MaterialPermScanWifiOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPermScanWifiOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPermScanWifiOutlinedIcon = MaterialPermScanWifiOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
