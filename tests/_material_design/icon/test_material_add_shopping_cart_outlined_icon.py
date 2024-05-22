from apysc._material_design.icon.material_add_shopping_cart_outlined_icon import (
    MaterialAddShoppingCartOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAddShoppingCartOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAddShoppingCartOutlinedIcon = (
            MaterialAddShoppingCartOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
