from apysc._material_design.icon.material_settings_bluetooth_icon import (
    MaterialSettingsBluetoothIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsBluetoothIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsBluetoothIcon = MaterialSettingsBluetoothIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
