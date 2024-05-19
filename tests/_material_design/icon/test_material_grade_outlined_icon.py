from apysc._material_design.icon.material_grade_outlined_icon import MaterialgradeOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialgradeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialgradeOutlinedIcon = MaterialgradeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
