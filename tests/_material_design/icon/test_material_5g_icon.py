from apysc._material_design.icon.material_5g_icon import Material5GIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial5GIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material5GIcon = Material5GIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
