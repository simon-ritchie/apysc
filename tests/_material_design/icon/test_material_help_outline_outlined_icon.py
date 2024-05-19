from apysc._material_design.icon.material_help_outline_outlined_icon import (
    MaterialhelpOutlineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhelpOutlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhelpOutlineOutlinedIcon = MaterialhelpOutlineOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
