from apysc._material_design.icon.material_flight_land_icon import MaterialflightLandIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialflightLandIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialflightLandIcon = MaterialflightLandIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
