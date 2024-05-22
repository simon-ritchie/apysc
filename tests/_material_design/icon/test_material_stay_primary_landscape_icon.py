from apysc._material_design.icon.material_stay_primary_landscape_icon import (
    MaterialStayPrimaryLandscapeIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialStayPrimaryLandscapeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialStayPrimaryLandscapeIcon = MaterialStayPrimaryLandscapeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
