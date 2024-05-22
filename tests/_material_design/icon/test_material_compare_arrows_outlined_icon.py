from apysc._material_design.icon.material_compare_arrows_outlined_icon import (
    MaterialCompareArrowsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCompareArrowsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCompareArrowsOutlinedIcon = MaterialCompareArrowsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
