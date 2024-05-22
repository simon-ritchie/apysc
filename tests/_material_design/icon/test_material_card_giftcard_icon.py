from apysc._material_design.icon.material_card_giftcard_icon import (
    MaterialCardGiftcardIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCardGiftcardIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCardGiftcardIcon = MaterialCardGiftcardIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
