from apysc._material_design.icon.material_payment_outlined_icon import MaterialpaymentOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpaymentOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpaymentOutlinedIcon = MaterialpaymentOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
