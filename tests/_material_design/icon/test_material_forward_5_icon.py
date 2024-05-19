from apysc._material_design.icon.material_forward_5_icon import Materialforward5Icon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialforward5Icon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Materialforward5Icon = Materialforward5Icon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
