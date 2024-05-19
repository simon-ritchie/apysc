from apysc._material_design.icon.material_4k_icon import Material4KIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial4KIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material4KIcon = Material4KIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
