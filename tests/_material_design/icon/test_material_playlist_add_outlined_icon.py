from apysc._material_design.icon.material_playlist_add_outlined_icon import (
    MaterialPlaylistAddOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPlaylistAddOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPlaylistAddOutlinedIcon = MaterialPlaylistAddOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
