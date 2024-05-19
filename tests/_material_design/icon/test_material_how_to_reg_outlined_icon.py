from apysc._material_design.icon.material_how_to_reg_outlined_icon import (
    MaterialhowToRegOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhowToRegOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhowToRegOutlinedIcon = MaterialhowToRegOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
