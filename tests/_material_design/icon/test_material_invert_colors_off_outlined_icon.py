from apysc._material_design.icon.material_invert_colors_off_outlined_icon import MaterialinvertColorsOffOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialinvertColorsOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialinvertColorsOffOutlinedIcon = MaterialinvertColorsOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
