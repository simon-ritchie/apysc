from apysc._material_design.icon.material_next_plan_icon import MaterialnextPlanIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnextPlanIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnextPlanIcon = MaterialnextPlanIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
