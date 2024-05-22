from apysc._material_design.icon.material_redeem_outlined_icon import (
    MaterialRedeemOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRedeemOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRedeemOutlinedIcon = MaterialRedeemOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
