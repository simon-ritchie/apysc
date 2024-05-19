from apysc._material_design.icon.material_5k_plus_icon import Material5KPlusIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial5KPlusIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material5KPlusIcon = Material5KPlusIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
