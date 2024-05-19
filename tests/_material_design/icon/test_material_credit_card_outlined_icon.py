from apysc._material_design.icon.material_credit_card_outlined_icon import (
    MaterialcreditCardOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcreditCardOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcreditCardOutlinedIcon = MaterialcreditCardOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
