from apysc._material_design.icon.material_7k_icon import Material7KIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial7KIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material7KIcon = Material7KIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
