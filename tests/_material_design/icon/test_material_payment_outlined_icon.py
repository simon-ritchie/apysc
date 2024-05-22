from apysc._material_design.icon.material_payment_outlined_icon import (
    MaterialPaymentOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPaymentOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPaymentOutlinedIcon = MaterialPaymentOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
