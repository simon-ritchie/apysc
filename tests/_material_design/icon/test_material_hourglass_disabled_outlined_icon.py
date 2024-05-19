from apysc._material_design.icon.material_hourglass_disabled_outlined_icon import MaterialhourglassDisabledOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhourglassDisabledOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhourglassDisabledOutlinedIcon = MaterialhourglassDisabledOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
