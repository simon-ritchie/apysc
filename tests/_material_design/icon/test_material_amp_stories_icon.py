from apysc._material_design.icon.material_amp_stories_icon import MaterialampStoriesIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialampStoriesIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialampStoriesIcon = MaterialampStoriesIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
