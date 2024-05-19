from apysc._material_design.icon.material_flight_land_outlined_icon import MaterialflightLandOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialflightLandOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialflightLandOutlinedIcon = MaterialflightLandOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
