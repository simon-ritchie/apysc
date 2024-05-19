from apysc._material_design.icon.material_portable_wifi_off_icon import MaterialportableWifiOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialportableWifiOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialportableWifiOffIcon = MaterialportableWifiOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
