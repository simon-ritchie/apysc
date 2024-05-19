from apysc._material_design.icon.material_swap_vertical_circle_outlined_icon import (
    MaterialswapVerticalCircleOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialswapVerticalCircleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialswapVerticalCircleOutlinedIcon = (
            MaterialswapVerticalCircleOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
