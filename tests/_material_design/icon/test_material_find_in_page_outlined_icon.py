from apysc._material_design.icon.material_find_in_page_outlined_icon import (
    MaterialFindInPageOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFindInPageOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFindInPageOutlinedIcon = MaterialFindInPageOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
