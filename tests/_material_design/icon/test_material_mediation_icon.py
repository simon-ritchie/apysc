from apysc._material_design.icon.material_mediation_icon import MaterialMediationIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMediationIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMediationIcon = MaterialMediationIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
