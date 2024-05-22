from apysc._material_design.icon.material_view_sidebar_icon import (
    MaterialViewSidebarIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialViewSidebarIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialViewSidebarIcon = MaterialViewSidebarIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
