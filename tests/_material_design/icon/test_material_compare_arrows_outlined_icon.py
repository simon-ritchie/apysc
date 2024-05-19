from apysc._material_design.icon.material_compare_arrows_outlined_icon import (
    MaterialcompareArrowsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcompareArrowsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcompareArrowsOutlinedIcon = MaterialcompareArrowsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
