from apysc._material_design.icon.material_mediation_outlined_icon import (
    MaterialmediationOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmediationOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmediationOutlinedIcon = MaterialmediationOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
