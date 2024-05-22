from apysc._material_design.icon.material_forward_10_icon import MaterialForward10Icon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialForward10Icon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialForward10Icon = MaterialForward10Icon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
