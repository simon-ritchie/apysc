from apysc._material_design.icon.material_forward_30_icon import MaterialForward30Icon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialForward30Icon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialForward30Icon = MaterialForward30Icon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
