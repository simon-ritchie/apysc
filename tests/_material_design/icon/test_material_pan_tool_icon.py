from apysc._material_design.icon.material_pan_tool_icon import MaterialpanToolIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpanToolIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpanToolIcon = MaterialpanToolIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
