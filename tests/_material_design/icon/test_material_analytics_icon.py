from apysc._material_design.icon.material_analytics_icon import MaterialanalyticsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialanalyticsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialanalyticsIcon = MaterialanalyticsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
