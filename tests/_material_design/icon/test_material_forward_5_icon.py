from apysc._material_design.icon.material_forward_5_icon import MaterialForward5Icon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialForward5Icon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialForward5Icon = MaterialForward5Icon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
