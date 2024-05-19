from apysc._material_design.icon.material_2k_icon import Material2KIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial2KIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material2KIcon = Material2KIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
