from apysc._material_design.icon.material_invert_colors_off_icon import MaterialinvertColorsOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialinvertColorsOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialinvertColorsOffIcon = MaterialinvertColorsOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
