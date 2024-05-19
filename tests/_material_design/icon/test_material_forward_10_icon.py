from apysc._material_design.icon.material_forward_10_icon import Materialforward10Icon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialforward10Icon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Materialforward10Icon = Materialforward10Icon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
