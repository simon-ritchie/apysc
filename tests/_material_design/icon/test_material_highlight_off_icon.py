from apysc._material_design.icon.material_highlight_off_icon import MaterialhighlightOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhighlightOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhighlightOffIcon = MaterialhighlightOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
