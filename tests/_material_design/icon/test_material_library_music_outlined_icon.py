from apysc._material_design.icon.material_library_music_outlined_icon import (
    MateriallibraryMusicOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallibraryMusicOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallibraryMusicOutlinedIcon = MateriallibraryMusicOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
