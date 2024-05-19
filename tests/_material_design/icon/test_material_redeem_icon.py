from apysc._material_design.icon.material_redeem_icon import MaterialredeemIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialredeemIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialredeemIcon = MaterialredeemIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
