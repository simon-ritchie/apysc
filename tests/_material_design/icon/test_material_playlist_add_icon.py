from apysc._material_design.icon.material_playlist_add_icon import (
    MaterialPlaylistAddIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPlaylistAddIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPlaylistAddIcon = MaterialPlaylistAddIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
