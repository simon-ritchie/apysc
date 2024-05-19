from apysc._material_design.icon.material_playlist_play_icon import (
    MaterialplaylistPlayIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialplaylistPlayIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialplaylistPlayIcon = MaterialplaylistPlayIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
