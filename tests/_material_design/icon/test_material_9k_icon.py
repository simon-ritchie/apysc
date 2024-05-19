from apysc._material_design.icon.material_9k_icon import Material9KIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial9KIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material9KIcon = Material9KIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
