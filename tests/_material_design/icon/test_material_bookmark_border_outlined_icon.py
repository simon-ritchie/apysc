from apysc._material_design.icon.material_bookmark_border_outlined_icon import (
    MaterialBookmarkBorderOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBookmarkBorderOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBookmarkBorderOutlinedIcon = MaterialBookmarkBorderOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
