from apysc._material_design.icon.material_forward_icon import MaterialForwardIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialForwardIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialForwardIcon = MaterialForwardIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
