from apysc._material_design.icon.material_analytics_outlined_icon import MaterialanalyticsOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialanalyticsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialanalyticsOutlinedIcon = MaterialanalyticsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
