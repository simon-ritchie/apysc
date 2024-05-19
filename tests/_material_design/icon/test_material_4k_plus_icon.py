from apysc._material_design.icon.material_4k_plus_icon import Material4KPlusIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial4KPlusIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material4KPlusIcon = Material4KPlusIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
