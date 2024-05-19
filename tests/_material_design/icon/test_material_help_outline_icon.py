from apysc._material_design.icon.material_help_outline_icon import (
    MaterialhelpOutlineIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhelpOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhelpOutlineIcon = MaterialhelpOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
