from apysc._material_design.icon.material_swap_horiz_outlined_icon import (
    MaterialswapHorizOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialswapHorizOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialswapHorizOutlinedIcon = MaterialswapHorizOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
