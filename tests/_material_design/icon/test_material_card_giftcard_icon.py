from apysc._material_design.icon.material_card_giftcard_icon import (
    MaterialcardGiftcardIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcardGiftcardIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcardGiftcardIcon = MaterialcardGiftcardIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
