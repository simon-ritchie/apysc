from apysc._material_design.icon.material_input_outlined_icon import MaterialinputOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialinputOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialinputOutlinedIcon = MaterialinputOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
