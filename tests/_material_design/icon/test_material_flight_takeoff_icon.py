from apysc._material_design.icon.material_flight_takeoff_icon import (
    MaterialFlightTakeoffIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFlightTakeoffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFlightTakeoffIcon = MaterialFlightTakeoffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
