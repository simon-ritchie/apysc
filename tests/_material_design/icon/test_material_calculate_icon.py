from apysc._material_design.icon.material_calculate_icon import MaterialcalculateIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcalculateIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcalculateIcon = MaterialcalculateIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
