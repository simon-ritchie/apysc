from apysc._material_design.icon.material_analytics_outlined_icon import (
    MaterialAnalyticsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAnalyticsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAnalyticsOutlinedIcon = MaterialAnalyticsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
