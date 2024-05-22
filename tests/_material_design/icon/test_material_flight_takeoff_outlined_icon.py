from apysc._material_design.icon.material_flight_takeoff_outlined_icon import (
    MaterialFlightTakeoffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFlightTakeoffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFlightTakeoffOutlinedIcon = MaterialFlightTakeoffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
