from apysc._material_design.icon.material_music_video_icon import MaterialMusicVideoIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMusicVideoIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMusicVideoIcon = MaterialMusicVideoIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
