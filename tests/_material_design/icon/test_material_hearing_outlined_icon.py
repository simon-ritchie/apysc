from apysc._material_design.icon.material_hearing_outlined_icon import MaterialhearingOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhearingOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhearingOutlinedIcon = MaterialhearingOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
