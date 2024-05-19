from apysc._material_design.icon.material_1k_plus_icon import Material1KPlusIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial1KPlusIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material1KPlusIcon = Material1KPlusIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
