from apysc._material_design.icon.material_forward_5_outlined_icon import (
    MaterialForward5OutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialForward5OutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialForward5OutlinedIcon = MaterialForward5OutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
