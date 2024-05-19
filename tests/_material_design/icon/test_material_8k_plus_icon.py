from apysc._material_design.icon.material_8k_plus_icon import Material8KPlusIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial8KPlusIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material8KPlusIcon = Material8KPlusIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
