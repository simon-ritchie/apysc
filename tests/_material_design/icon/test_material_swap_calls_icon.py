from apysc._material_design.icon.material_swap_calls_icon import MaterialswapCallsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialswapCallsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialswapCallsIcon = MaterialswapCallsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
