from apysc._material_design.icon.material_compare_arrows_icon import (
    MaterialcompareArrowsIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcompareArrowsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcompareArrowsIcon = MaterialcompareArrowsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
