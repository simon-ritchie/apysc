from apysc._material_design.icon.material_invert_colors_outlined_icon import MaterialinvertColorsOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialinvertColorsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialinvertColorsOutlinedIcon = MaterialinvertColorsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
