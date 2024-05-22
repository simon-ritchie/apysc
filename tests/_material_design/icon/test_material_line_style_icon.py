from apysc._material_design.icon.material_line_style_icon import MaterialLineStyleIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLineStyleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLineStyleIcon = MaterialLineStyleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
