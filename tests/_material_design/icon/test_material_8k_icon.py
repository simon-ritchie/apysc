from apysc._material_design.icon.material_8k_icon import Material8KIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial8KIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material8KIcon = Material8KIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
