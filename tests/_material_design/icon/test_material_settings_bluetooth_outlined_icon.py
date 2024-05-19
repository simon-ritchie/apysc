from apysc._material_design.icon.material_settings_bluetooth_outlined_icon import MaterialsettingsBluetoothOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsBluetoothOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsBluetoothOutlinedIcon = MaterialsettingsBluetoothOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
