from apysc._material_design.icon.material_fiber_pin_icon import MaterialfiberPinIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfiberPinIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfiberPinIcon = MaterialfiberPinIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
