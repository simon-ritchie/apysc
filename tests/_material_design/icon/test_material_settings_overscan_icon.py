from apysc._material_design.icon.material_settings_overscan_icon import MaterialsettingsOverscanIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsOverscanIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsOverscanIcon = MaterialsettingsOverscanIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
