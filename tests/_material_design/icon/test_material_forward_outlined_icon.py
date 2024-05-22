from apysc._material_design.icon.material_forward_outlined_icon import (
    MaterialForwardOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialForwardOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialForwardOutlinedIcon = MaterialForwardOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
