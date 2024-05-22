from apysc._material_design.icon.material_swap_calls_outlined_icon import (
    MaterialSwapCallsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSwapCallsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSwapCallsOutlinedIcon = MaterialSwapCallsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
