from apysc._material_design.icon.material_shopping_bag_icon import MaterialshoppingBagIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialshoppingBagIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialshoppingBagIcon = MaterialshoppingBagIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
