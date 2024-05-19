from apysc._material_design.icon.material_settings_power_icon import MaterialsettingsPowerIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsPowerIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsPowerIcon = MaterialsettingsPowerIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
