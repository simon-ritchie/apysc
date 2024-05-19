from apysc._material_design.icon.material_swap_vert_outlined_icon import MaterialswapVertOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialswapVertOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialswapVertOutlinedIcon = MaterialswapVertOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
