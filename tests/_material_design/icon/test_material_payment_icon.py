from apysc._material_design.icon.material_payment_icon import MaterialpaymentIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpaymentIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpaymentIcon = MaterialpaymentIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
