from apysc._material_design.icon.material_dashboard_customize_icon import MaterialdashboardCustomizeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdashboardCustomizeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdashboardCustomizeIcon = MaterialdashboardCustomizeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
