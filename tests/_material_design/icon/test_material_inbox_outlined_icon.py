from apysc._material_design.icon.material_inbox_outlined_icon import (
    MaterialinboxOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialinboxOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialinboxOutlinedIcon = MaterialinboxOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
