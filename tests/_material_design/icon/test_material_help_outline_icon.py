from apysc._material_design.icon.material_help_outline_icon import (
    MaterialHelpOutlineIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHelpOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHelpOutlineIcon = MaterialHelpOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
