from apysc._material_design.icon.material_compare_arrows_icon import (
    MaterialCompareArrowsIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCompareArrowsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCompareArrowsIcon = MaterialCompareArrowsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
