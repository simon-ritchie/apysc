from apysc._material_design.icon.material_calculate_icon import MaterialCalculateIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCalculateIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCalculateIcon = MaterialCalculateIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
