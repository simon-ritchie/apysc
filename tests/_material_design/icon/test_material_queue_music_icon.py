from apysc._material_design.icon.material_queue_music_icon import MaterialqueueMusicIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialqueueMusicIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialqueueMusicIcon = MaterialqueueMusicIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
