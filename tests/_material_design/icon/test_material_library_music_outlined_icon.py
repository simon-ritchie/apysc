from apysc._material_design.icon.material_library_music_outlined_icon import (
    MaterialLibraryMusicOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLibraryMusicOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLibraryMusicOutlinedIcon = MaterialLibraryMusicOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
