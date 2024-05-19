from apysc._material_design.icon.material_remove_shopping_cart_icon import MaterialremoveShoppingCartIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialremoveShoppingCartIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialremoveShoppingCartIcon = MaterialremoveShoppingCartIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
