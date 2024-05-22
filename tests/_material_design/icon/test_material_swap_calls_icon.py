from apysc._material_design.icon.material_swap_calls_icon import MaterialSwapCallsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSwapCallsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSwapCallsIcon = MaterialSwapCallsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
