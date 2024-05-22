from apysc._material_design.icon.material_swap_horiz_outlined_icon import (
    MaterialSwapHorizOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSwapHorizOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSwapHorizOutlinedIcon = MaterialSwapHorizOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
