from apysc._material_design.icon.material_swap_vertical_circle_outlined_icon import (
    MaterialSwapVerticalCircleOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSwapVerticalCircleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSwapVerticalCircleOutlinedIcon = (
            MaterialSwapVerticalCircleOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
