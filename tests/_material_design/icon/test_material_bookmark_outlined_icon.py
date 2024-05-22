from apysc._material_design.icon.material_bookmark_outlined_icon import (
    MaterialBookmarkOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBookmarkOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBookmarkOutlinedIcon = MaterialBookmarkOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
