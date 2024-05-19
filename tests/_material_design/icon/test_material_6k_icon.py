from apysc._material_design.icon.material_6k_icon import Material6KIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial6KIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material6KIcon = Material6KIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
