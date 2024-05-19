from apysc._material_design.icon.material_featured_video_icon import (
    MaterialfeaturedVideoIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfeaturedVideoIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfeaturedVideoIcon = MaterialfeaturedVideoIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
