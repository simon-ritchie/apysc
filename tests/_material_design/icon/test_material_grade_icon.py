from apysc._material_design.icon.material_grade_icon import MaterialgradeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialgradeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialgradeIcon = MaterialgradeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
