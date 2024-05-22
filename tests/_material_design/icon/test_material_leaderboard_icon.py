from apysc._material_design.icon.material_leaderboard_icon import (
    MaterialLeaderboardIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLeaderboardIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLeaderboardIcon = MaterialLeaderboardIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
