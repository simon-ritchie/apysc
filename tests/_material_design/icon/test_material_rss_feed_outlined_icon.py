from apysc._material_design.icon.material_rss_feed_outlined_icon import (
    MaterialRssFeedOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRssFeedOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRssFeedOutlinedIcon = MaterialRssFeedOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
