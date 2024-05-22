from apysc._material_design.icon.material_filter_list_outlined_icon import (
    MaterialFilterListOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFilterListOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFilterListOutlinedIcon = MaterialFilterListOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
