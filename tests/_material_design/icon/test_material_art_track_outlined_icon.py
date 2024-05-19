from apysc._material_design.icon.material_art_track_outlined_icon import (
    MaterialartTrackOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialartTrackOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialartTrackOutlinedIcon = MaterialartTrackOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
