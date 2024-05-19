from apysc._material_design.icon.material_help_outlined_icon import (
    MaterialhelpOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhelpOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhelpOutlinedIcon = MaterialhelpOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
