from apysc._material_design.icon.material_hourglass_top_outlined_icon import MaterialhourglassTopOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhourglassTopOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhourglassTopOutlinedIcon = MaterialhourglassTopOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
