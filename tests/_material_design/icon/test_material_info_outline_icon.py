from apysc._material_design.icon.material_info_outline_icon import (
    MaterialinfoOutlineIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialinfoOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialinfoOutlineIcon = MaterialinfoOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
