from apysc._material_design.icon.material_shop_two_outlined_icon import MaterialshopTwoOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialshopTwoOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialshopTwoOutlinedIcon = MaterialshopTwoOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
