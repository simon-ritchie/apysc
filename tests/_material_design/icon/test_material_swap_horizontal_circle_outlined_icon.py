from apysc._material_design.icon.material_swap_horizontal_circle_outlined_icon import (
    MaterialSwapHorizontalCircleOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSwapHorizontalCircleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSwapHorizontalCircleOutlinedIcon = (
            MaterialSwapHorizontalCircleOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
