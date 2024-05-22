from apysc._material_design.icon.material_rule_icon import MaterialRuleIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRuleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRuleIcon = MaterialRuleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
