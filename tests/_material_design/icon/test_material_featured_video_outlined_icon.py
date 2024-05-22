from apysc._material_design.icon.material_featured_video_outlined_icon import (
    MaterialFeaturedVideoOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFeaturedVideoOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFeaturedVideoOutlinedIcon = MaterialFeaturedVideoOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
