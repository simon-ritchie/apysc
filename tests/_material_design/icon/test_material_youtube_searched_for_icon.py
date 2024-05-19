from apysc._material_design.icon.material_youtube_searched_for_icon import (
    MaterialyoutubeSearchedForIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialyoutubeSearchedForIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialyoutubeSearchedForIcon = MaterialyoutubeSearchedForIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
