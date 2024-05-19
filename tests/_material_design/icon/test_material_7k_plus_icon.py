from apysc._material_design.icon.material_7k_plus_icon import Material7KPlusIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial7KPlusIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material7KPlusIcon = Material7KPlusIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
