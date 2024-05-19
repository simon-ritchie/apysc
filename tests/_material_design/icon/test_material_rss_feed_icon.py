from apysc._material_design.icon.material_rss_feed_icon import MaterialrssFeedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialrssFeedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialrssFeedIcon = MaterialrssFeedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
