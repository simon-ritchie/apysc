from apysc._material_design.icon.material_help_center_outlined_icon import MaterialhelpCenterOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhelpCenterOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhelpCenterOutlinedIcon = MaterialhelpCenterOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
