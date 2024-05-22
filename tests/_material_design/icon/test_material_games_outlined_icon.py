from apysc._material_design.icon.material_games_outlined_icon import (
    MaterialGamesOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialGamesOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialGamesOutlinedIcon = MaterialGamesOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
