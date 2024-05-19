from apysc._material_design.icon.material_subtitles_icon import MaterialsubtitlesIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsubtitlesIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsubtitlesIcon = MaterialsubtitlesIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
