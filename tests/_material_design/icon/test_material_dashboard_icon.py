from apysc._material_design.icon.material_dashboard_icon import MaterialdashboardIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdashboardIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdashboardIcon = MaterialdashboardIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
