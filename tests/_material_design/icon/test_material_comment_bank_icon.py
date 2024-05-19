from apysc._material_design.icon.material_comment_bank_icon import MaterialcommentBankIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcommentBankIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcommentBankIcon = MaterialcommentBankIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
