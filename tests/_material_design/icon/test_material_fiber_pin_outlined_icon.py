from apysc._material_design.icon.material_fiber_pin_outlined_icon import MaterialfiberPinOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfiberPinOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfiberPinOutlinedIcon = MaterialfiberPinOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
