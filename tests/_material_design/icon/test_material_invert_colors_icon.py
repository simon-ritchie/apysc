from apysc._material_design.icon.material_invert_colors_icon import MaterialinvertColorsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialinvertColorsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialinvertColorsIcon = MaterialinvertColorsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
