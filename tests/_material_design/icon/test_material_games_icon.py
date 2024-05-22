from apysc._material_design.icon.material_games_icon import MaterialGamesIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialGamesIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialGamesIcon = MaterialGamesIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
