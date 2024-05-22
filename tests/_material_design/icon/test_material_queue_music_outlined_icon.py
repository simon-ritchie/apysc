from apysc._material_design.icon.material_queue_music_outlined_icon import (
    MaterialQueueMusicOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialQueueMusicOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialQueueMusicOutlinedIcon = MaterialQueueMusicOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
