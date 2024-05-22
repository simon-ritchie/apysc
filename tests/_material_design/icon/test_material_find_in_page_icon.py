from apysc._material_design.icon.material_find_in_page_icon import (
    MaterialFindInPageIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFindInPageIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFindInPageIcon = MaterialFindInPageIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
