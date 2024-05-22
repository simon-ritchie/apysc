from apysc._material_design.icon.material_playlist_play_icon import (
    MaterialPlaylistPlayIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPlaylistPlayIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPlaylistPlayIcon = MaterialPlaylistPlayIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
