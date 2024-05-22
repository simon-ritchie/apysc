from apysc._material_design.icon.material_comment_icon import MaterialCommentIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCommentIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCommentIcon = MaterialCommentIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
