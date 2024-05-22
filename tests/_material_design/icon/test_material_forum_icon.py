from apysc._material_design.icon.material_forum_icon import MaterialForumIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialForumIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialForumIcon = MaterialForumIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
