from apysc._material_design.icon.material_dashboard_outlined_icon import (
    MaterialDashboardOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDashboardOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDashboardOutlinedIcon = MaterialDashboardOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
