from apysc._material_design.icon.material_dynamic_feed_icon import MaterialdynamicFeedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdynamicFeedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdynamicFeedIcon = MaterialdynamicFeedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
