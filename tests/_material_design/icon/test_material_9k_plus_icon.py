from apysc._material_design.icon.material_9k_plus_icon import Material9KPlusIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial9KPlusIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material9KPlusIcon = Material9KPlusIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
