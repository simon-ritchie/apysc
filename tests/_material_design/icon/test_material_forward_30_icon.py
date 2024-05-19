from apysc._material_design.icon.material_forward_30_icon import Materialforward30Icon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialforward30Icon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Materialforward30Icon = Materialforward30Icon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
