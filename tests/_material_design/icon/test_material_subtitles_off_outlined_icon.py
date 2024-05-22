from apysc._material_design.icon.material_subtitles_off_outlined_icon import (
    MaterialSubtitlesOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSubtitlesOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSubtitlesOffOutlinedIcon = MaterialSubtitlesOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
