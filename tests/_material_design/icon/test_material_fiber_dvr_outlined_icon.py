from apysc._material_design.icon.material_fiber_dvr_outlined_icon import (
    MaterialFiberDvrOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFiberDvrOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFiberDvrOutlinedIcon = MaterialFiberDvrOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
