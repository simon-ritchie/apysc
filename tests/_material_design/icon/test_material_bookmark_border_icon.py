from apysc._material_design.icon.material_bookmark_border_icon import (
    MaterialBookmarkBorderIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBookmarkBorderIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBookmarkBorderIcon = MaterialBookmarkBorderIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
