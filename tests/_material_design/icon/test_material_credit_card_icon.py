from apysc._material_design.icon.material_credit_card_icon import MaterialcreditCardIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcreditCardIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcreditCardIcon = MaterialcreditCardIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
