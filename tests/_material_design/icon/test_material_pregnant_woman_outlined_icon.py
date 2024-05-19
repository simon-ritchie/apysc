from apysc._material_design.icon.material_pregnant_woman_outlined_icon import MaterialpregnantWomanOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpregnantWomanOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpregnantWomanOutlinedIcon = MaterialpregnantWomanOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
