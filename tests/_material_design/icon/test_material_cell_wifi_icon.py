from apysc._material_design.icon.material_cell_wifi_icon import MaterialCellWifiIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCellWifiIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCellWifiIcon = MaterialCellWifiIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
