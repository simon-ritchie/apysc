from apysc._material_design.icon.material_bookmarks_icon import MaterialbookmarksIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbookmarksIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbookmarksIcon = MaterialbookmarksIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
