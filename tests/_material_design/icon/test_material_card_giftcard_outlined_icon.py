from apysc._material_design.icon.material_card_giftcard_outlined_icon import MaterialcardGiftcardOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcardGiftcardOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcardGiftcardOutlinedIcon = MaterialcardGiftcardOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
