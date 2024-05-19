from apysc._material_design.icon.material_shopping_basket_icon import MaterialshoppingBasketIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialshoppingBasketIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialshoppingBasketIcon = MaterialshoppingBasketIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
