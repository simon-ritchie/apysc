from apysc._material_design.icon.material_swap_vert_icon import MaterialswapVertIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialswapVertIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialswapVertIcon = MaterialswapVertIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
