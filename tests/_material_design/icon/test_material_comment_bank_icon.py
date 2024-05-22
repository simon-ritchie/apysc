from apysc._material_design.icon.material_comment_bank_icon import (
    MaterialCommentBankIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCommentBankIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCommentBankIcon = MaterialCommentBankIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
