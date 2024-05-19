from apysc._material_design.icon.material_line_style_icon import MateriallineStyleIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallineStyleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallineStyleIcon = MateriallineStyleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
