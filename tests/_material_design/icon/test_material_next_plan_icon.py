from apysc._material_design.icon.material_next_plan_icon import MaterialNextPlanIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialNextPlanIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialNextPlanIcon = MaterialNextPlanIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
