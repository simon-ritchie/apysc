from apysc._material_design.icon.material_swap_vertical_circle_icon import (
    MaterialSwapVerticalCircleIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSwapVerticalCircleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSwapVerticalCircleIcon = MaterialSwapVerticalCircleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
