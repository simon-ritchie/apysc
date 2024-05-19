from apysc._material_design.icon.material_swap_horiz_icon import MaterialswapHorizIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialswapHorizIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialswapHorizIcon = MaterialswapHorizIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
