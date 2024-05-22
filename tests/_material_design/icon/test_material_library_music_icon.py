from apysc._material_design.icon.material_library_music_icon import (
    MaterialLibraryMusicIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLibraryMusicIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLibraryMusicIcon = MaterialLibraryMusicIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
