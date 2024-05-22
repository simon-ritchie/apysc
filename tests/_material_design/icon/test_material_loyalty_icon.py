from apysc._material_design.icon.material_loyalty_icon import MaterialLoyaltyIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLoyaltyIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLoyaltyIcon = MaterialLoyaltyIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
