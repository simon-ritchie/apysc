from apysc._material_design.icon.material_5g_outlined_icon import Material5GOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterial5GOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: Material5GOutlinedIcon = Material5GOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
