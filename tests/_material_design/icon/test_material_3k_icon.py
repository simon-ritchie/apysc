from apysc._material_design.icon.material_3k_icon import Material3KIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial3KIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material3KIcon = Material3KIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
