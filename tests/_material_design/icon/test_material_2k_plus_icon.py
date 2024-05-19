from apysc._material_design.icon.material_2k_plus_icon import Material2KPlusIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial2KPlusIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material2KPlusIcon = Material2KPlusIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
