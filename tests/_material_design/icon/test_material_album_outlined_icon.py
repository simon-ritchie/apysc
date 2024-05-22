from apysc._material_design.icon.material_album_outlined_icon import (
    MaterialAlbumOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAlbumOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAlbumOutlinedIcon = MaterialAlbumOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
