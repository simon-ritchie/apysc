from apysc._material_design.icon.material_forward_10_outlined_icon import (
    Materialforward10OutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialforward10OutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Materialforward10OutlinedIcon = Materialforward10OutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
