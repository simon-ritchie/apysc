from apysc._material_design.icon.material_fiber_dvr_icon import MaterialfiberDvrIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfiberDvrIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfiberDvrIcon = MaterialfiberDvrIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
