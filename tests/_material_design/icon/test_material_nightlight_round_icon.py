from apysc._material_design.icon.material_nightlight_round_icon import MaterialnightlightRoundIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnightlightRoundIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnightlightRoundIcon = MaterialnightlightRoundIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
