from apysc._material_design.icon.material_library_music_icon import (
    MateriallibraryMusicIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallibraryMusicIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallibraryMusicIcon = MateriallibraryMusicIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
