from apysc._material_design.icon.material_loyalty_outlined_icon import (
    MaterialLoyaltyOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLoyaltyOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLoyaltyOutlinedIcon = MaterialLoyaltyOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
