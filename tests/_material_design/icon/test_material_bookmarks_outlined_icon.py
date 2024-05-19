from apysc._material_design.icon.material_bookmarks_outlined_icon import MaterialbookmarksOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbookmarksOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbookmarksOutlinedIcon = MaterialbookmarksOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
