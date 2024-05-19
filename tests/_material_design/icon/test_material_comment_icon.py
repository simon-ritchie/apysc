from apysc._material_design.icon.material_comment_icon import MaterialcommentIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcommentIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcommentIcon = MaterialcommentIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
