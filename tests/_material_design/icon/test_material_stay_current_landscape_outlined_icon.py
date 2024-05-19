from apysc._material_design.icon.material_stay_current_landscape_outlined_icon import MaterialstayCurrentLandscapeOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialstayCurrentLandscapeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialstayCurrentLandscapeOutlinedIcon = MaterialstayCurrentLandscapeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
