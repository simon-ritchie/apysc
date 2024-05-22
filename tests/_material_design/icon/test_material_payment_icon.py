from apysc._material_design.icon.material_payment_icon import MaterialPaymentIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPaymentIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPaymentIcon = MaterialPaymentIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
