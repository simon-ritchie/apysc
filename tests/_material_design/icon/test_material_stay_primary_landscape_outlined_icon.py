from apysc._material_design.icon.material_stay_primary_landscape_outlined_icon import (
    MaterialStayPrimaryLandscapeOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialStayPrimaryLandscapeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialStayPrimaryLandscapeOutlinedIcon = (
            MaterialStayPrimaryLandscapeOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
