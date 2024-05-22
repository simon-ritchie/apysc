from apysc._material_design.icon.material_perm_scan_wifi_icon import (
    MaterialPermScanWifiIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPermScanWifiIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPermScanWifiIcon = MaterialPermScanWifiIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
