from apysc._material_design.icon.material_airplay_icon import MaterialAirplayIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAirplayIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAirplayIcon = MaterialAirplayIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
