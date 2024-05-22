from apysc._material_design.icon.material_fiber_pin_outlined_icon import (
    MaterialFiberPinOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFiberPinOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFiberPinOutlinedIcon = MaterialFiberPinOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
