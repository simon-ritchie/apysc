from apysc._material_design.icon.material_forward_30_outlined_icon import (
    MaterialForward30OutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialForward30OutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialForward30OutlinedIcon = MaterialForward30OutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
