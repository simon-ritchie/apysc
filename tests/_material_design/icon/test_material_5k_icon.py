from apysc._material_design.icon.material_5k_icon import Material5KIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial5KIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material5KIcon = Material5KIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
