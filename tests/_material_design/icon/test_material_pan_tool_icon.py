from apysc._material_design.icon.material_pan_tool_icon import MaterialPanToolIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPanToolIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPanToolIcon = MaterialPanToolIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
