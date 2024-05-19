from apysc._material_design.icon.material_redeem_outlined_icon import (
    MaterialredeemOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialredeemOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialredeemOutlinedIcon = MaterialredeemOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
