from apysc._material_design.icon.material_bookmarks_icon import MaterialBookmarksIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBookmarksIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBookmarksIcon = MaterialBookmarksIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
