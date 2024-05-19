from apysc._material_design.icon.material_6k_plus_icon import Material6KPlusIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial6KPlusIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material6KPlusIcon = Material6KPlusIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
