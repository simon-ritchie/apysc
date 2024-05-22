from apysc._material_design.icon.material_rss_feed_icon import MaterialRssFeedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRssFeedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRssFeedIcon = MaterialRssFeedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
