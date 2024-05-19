from apysc._material_design.icon.material_mediation_icon import MaterialmediationIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmediationIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmediationIcon = MaterialmediationIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
