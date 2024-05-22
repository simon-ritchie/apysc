from apysc._material_design.icon.material_next_plan_outlined_icon import (
    MaterialNextPlanOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialNextPlanOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialNextPlanOutlinedIcon = MaterialNextPlanOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
