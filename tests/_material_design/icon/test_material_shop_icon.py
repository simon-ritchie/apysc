from apysc._material_design.icon.material_shop_icon import MaterialShopIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialShopIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialShopIcon = MaterialShopIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
