from apysc._material_design.icon.material_featured_play_list_outlined_icon import (
    MaterialFeaturedPlayListOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFeaturedPlayListOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFeaturedPlayListOutlinedIcon = (
            MaterialFeaturedPlayListOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
