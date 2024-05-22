from apysc._material_design.icon.material_leaderboard_outlined_icon import (
    MaterialLeaderboardOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLeaderboardOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLeaderboardOutlinedIcon = MaterialLeaderboardOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
