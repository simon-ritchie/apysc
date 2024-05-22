from apysc._material_design.icon.material_shopping_bag_icon import (
    MaterialShoppingBagIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialShoppingBagIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialShoppingBagIcon = MaterialShoppingBagIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
