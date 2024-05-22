from apysc._material_design.icon.material_help_outlined_icon import (
    MaterialHelpOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHelpOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHelpOutlinedIcon = MaterialHelpOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
