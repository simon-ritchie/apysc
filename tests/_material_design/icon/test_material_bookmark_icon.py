from apysc._material_design.icon.material_bookmark_icon import MaterialBookmarkIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBookmarkIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBookmarkIcon = MaterialBookmarkIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
