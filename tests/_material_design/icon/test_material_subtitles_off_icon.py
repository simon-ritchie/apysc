from apysc._material_design.icon.material_subtitles_off_icon import (
    MaterialSubtitlesOffIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSubtitlesOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSubtitlesOffIcon = MaterialSubtitlesOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
