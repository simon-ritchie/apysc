from apysc._material_design.icon.material_subtitles_outlined_icon import (
    MaterialSubtitlesOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSubtitlesOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSubtitlesOutlinedIcon = MaterialSubtitlesOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
