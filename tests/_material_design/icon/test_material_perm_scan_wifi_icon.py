from apysc._material_design.icon.material_perm_scan_wifi_icon import MaterialpermScanWifiIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpermScanWifiIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpermScanWifiIcon = MaterialpermScanWifiIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
