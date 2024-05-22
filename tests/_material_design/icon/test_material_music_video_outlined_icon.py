from apysc._material_design.icon.material_music_video_outlined_icon import (
    MaterialMusicVideoOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMusicVideoOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMusicVideoOutlinedIcon = MaterialMusicVideoOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
