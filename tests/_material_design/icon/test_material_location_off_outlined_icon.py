from apysc._material_design.icon.material_location_off_outlined_icon import MateriallocationOffOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallocationOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallocationOffOutlinedIcon = MateriallocationOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
