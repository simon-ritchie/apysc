from apysc._material_design.icon.material_nat_icon import MaterialNatIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialNatIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialNatIcon = MaterialNatIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
