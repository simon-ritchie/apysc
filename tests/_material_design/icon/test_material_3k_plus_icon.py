from apysc._material_design.icon.material_3k_plus_icon import Material3KPlusIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial3KPlusIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material3KPlusIcon = Material3KPlusIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
