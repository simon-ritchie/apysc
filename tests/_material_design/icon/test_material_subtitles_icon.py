from apysc._material_design.icon.material_subtitles_icon import MaterialSubtitlesIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSubtitlesIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSubtitlesIcon = MaterialSubtitlesIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
