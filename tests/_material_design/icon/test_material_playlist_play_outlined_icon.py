from apysc._material_design.icon.material_playlist_play_outlined_icon import (
    MaterialPlaylistPlayOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPlaylistPlayOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPlaylistPlayOutlinedIcon = MaterialPlaylistPlayOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
