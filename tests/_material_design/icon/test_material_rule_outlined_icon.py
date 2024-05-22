from apysc._material_design.icon.material_rule_outlined_icon import (
    MaterialRuleOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRuleOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRuleOutlinedIcon = MaterialRuleOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
