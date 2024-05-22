from apysc._material_design.icon.material_amp_stories_icon import MaterialAmpStoriesIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAmpStoriesIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAmpStoriesIcon = MaterialAmpStoriesIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
