from apysc._material_design.icon.material_find_in_page_icon import (
    MaterialfindInPageIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfindInPageIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfindInPageIcon = MaterialfindInPageIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
