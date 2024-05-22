from apysc._material_design.icon.material_comment_bank_outlined_icon import (
    MaterialCommentBankOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCommentBankOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCommentBankOutlinedIcon = MaterialCommentBankOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
