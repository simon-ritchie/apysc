from apysc._material_design.icon.material_amp_stories_outlined_icon import (
    MaterialAmpStoriesOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAmpStoriesOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAmpStoriesOutlinedIcon = MaterialAmpStoriesOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
