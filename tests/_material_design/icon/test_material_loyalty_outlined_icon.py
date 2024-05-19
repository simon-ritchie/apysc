from apysc._material_design.icon.material_loyalty_outlined_icon import (
    MaterialloyaltyOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialloyaltyOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialloyaltyOutlinedIcon = MaterialloyaltyOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
