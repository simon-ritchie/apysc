from apysc._material_design.icon.material_shopping_basket_outlined_icon import (
    MaterialShoppingBasketOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialShoppingBasketOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialShoppingBasketOutlinedIcon = MaterialShoppingBasketOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
