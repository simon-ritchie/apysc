from apysc._material_design.icon.material_shopping_bag_outlined_icon import MaterialshoppingBagOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialshoppingBagOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialshoppingBagOutlinedIcon = MaterialshoppingBagOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
