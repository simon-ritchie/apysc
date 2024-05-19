from apysc._material_design.icon.material_stay_current_landscape_icon import (
    MaterialstayCurrentLandscapeIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialstayCurrentLandscapeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialstayCurrentLandscapeIcon = MaterialstayCurrentLandscapeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
