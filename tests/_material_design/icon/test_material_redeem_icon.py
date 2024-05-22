from apysc._material_design.icon.material_redeem_icon import MaterialRedeemIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRedeemIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRedeemIcon = MaterialRedeemIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
