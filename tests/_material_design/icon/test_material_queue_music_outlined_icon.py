from apysc._material_design.icon.material_queue_music_outlined_icon import MaterialqueueMusicOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialqueueMusicOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialqueueMusicOutlinedIcon = MaterialqueueMusicOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
