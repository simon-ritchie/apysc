from apysc._material_design.icon.material_add_shopping_cart_icon import MaterialaddShoppingCartIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaddShoppingCartIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaddShoppingCartIcon = MaterialaddShoppingCartIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
