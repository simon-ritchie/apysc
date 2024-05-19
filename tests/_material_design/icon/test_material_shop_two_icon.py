from apysc._material_design.icon.material_shop_two_icon import MaterialshopTwoIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialshopTwoIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialshopTwoIcon = MaterialshopTwoIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
