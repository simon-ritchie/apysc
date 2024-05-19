from apysc._material_design.icon.material_music_video_icon import MaterialmusicVideoIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmusicVideoIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmusicVideoIcon = MaterialmusicVideoIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
