from apysc._material_design.icon.material_highlight_alt_icon import MaterialhighlightAltIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhighlightAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhighlightAltIcon = MaterialhighlightAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
