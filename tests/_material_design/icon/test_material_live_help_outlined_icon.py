from apysc._material_design.icon.material_live_help_outlined_icon import MaterialliveHelpOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialliveHelpOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialliveHelpOutlinedIcon = MaterialliveHelpOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
