from apysc._material_design.icon.material_forum_outlined_icon import (
    MaterialforumOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialforumOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialforumOutlinedIcon = MaterialforumOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
