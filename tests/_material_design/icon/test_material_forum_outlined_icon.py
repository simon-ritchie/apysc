from apysc._material_design.icon.material_forum_outlined_icon import (
    MaterialForumOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialForumOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialForumOutlinedIcon = MaterialForumOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
