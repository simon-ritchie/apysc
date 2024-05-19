from apysc._material_design.icon.material_games_outlined_icon import (
    MaterialgamesOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialgamesOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialgamesOutlinedIcon = MaterialgamesOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
