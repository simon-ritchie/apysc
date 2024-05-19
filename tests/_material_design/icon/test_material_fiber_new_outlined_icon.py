from apysc._material_design.icon.material_fiber_new_outlined_icon import MaterialfiberNewOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfiberNewOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfiberNewOutlinedIcon = MaterialfiberNewOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
