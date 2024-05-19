from apysc._material_design.icon.material_search_outlined_icon import (
    MaterialsearchOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsearchOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsearchOutlinedIcon = MaterialsearchOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
