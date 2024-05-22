from apysc._material_design.icon.material_policy_icon import MaterialPolicyIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPolicyIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPolicyIcon = MaterialPolicyIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
