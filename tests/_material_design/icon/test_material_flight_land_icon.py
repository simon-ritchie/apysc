from apysc._material_design.icon.material_flight_land_icon import MaterialFlightLandIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFlightLandIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFlightLandIcon = MaterialFlightLandIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
