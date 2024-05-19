from apysc._material_design.icon.material_pan_tool_outlined_icon import MaterialpanToolOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpanToolOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpanToolOutlinedIcon = MaterialpanToolOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
