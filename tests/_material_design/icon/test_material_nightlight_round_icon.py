from apysc._material_design.icon.material_nightlight_round_icon import (
    MaterialNightlightRoundIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialNightlightRoundIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialNightlightRoundIcon = MaterialNightlightRoundIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
