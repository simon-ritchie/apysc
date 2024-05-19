from apysc._material_design.icon.material_view_sidebar_outlined_icon import (
    MaterialviewSidebarOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialviewSidebarOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialviewSidebarOutlinedIcon = MaterialviewSidebarOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
