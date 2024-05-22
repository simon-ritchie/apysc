from apysc._material_design.icon.material_insights_outlined_icon import (
    MaterialInsightsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialInsightsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialInsightsOutlinedIcon = MaterialInsightsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
