from apysc._material_design.icon.material_shopping_cart_icon import MaterialshoppingCartIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialshoppingCartIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialshoppingCartIcon = MaterialshoppingCartIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
