from apysc._material_design.icon.material_games_icon import MaterialgamesIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialgamesIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialgamesIcon = MaterialgamesIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
