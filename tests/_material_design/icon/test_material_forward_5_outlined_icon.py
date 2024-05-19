from apysc._material_design.icon.material_forward_5_outlined_icon import (
    Materialforward5OutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialforward5OutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Materialforward5OutlinedIcon = Materialforward5OutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
