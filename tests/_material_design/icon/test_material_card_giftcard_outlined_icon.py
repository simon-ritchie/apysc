from apysc._material_design.icon.material_card_giftcard_outlined_icon import (
    MaterialCardGiftcardOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCardGiftcardOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCardGiftcardOutlinedIcon = MaterialCardGiftcardOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
