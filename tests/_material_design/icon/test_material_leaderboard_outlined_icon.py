from apysc._material_design.icon.material_leaderboard_outlined_icon import (
    MaterialleaderboardOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialleaderboardOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialleaderboardOutlinedIcon = MaterialleaderboardOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
