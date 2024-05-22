from apysc._material_design.icon.material_remove_shopping_cart_icon import (
    MaterialRemoveShoppingCartIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRemoveShoppingCartIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRemoveShoppingCartIcon = MaterialRemoveShoppingCartIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
