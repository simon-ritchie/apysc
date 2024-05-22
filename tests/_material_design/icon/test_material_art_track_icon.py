from apysc._material_design.icon.material_art_track_icon import MaterialArtTrackIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialArtTrackIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialArtTrackIcon = MaterialArtTrackIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
