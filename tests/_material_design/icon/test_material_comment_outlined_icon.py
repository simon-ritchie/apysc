from apysc._material_design.icon.material_comment_outlined_icon import (
    MaterialCommentOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCommentOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCommentOutlinedIcon = MaterialCommentOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
