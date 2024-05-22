from apysc._material_design.icon.material_help_outline_outlined_icon import (
    MaterialHelpOutlineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHelpOutlineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHelpOutlineOutlinedIcon = MaterialHelpOutlineOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
