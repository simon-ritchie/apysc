from apysc._material_design.icon.material_line_style_outlined_icon import MateriallineStyleOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallineStyleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallineStyleOutlinedIcon = MateriallineStyleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
