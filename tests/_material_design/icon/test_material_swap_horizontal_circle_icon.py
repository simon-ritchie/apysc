from apysc._material_design.icon.material_swap_horizontal_circle_icon import MaterialswapHorizontalCircleIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialswapHorizontalCircleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialswapHorizontalCircleIcon = MaterialswapHorizontalCircleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
