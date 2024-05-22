from apysc._material_design.icon.material_dynamic_feed_icon import (
    MaterialDynamicFeedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDynamicFeedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDynamicFeedIcon = MaterialDynamicFeedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
