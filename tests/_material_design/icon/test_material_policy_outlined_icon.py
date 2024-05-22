from apysc._material_design.icon.material_policy_outlined_icon import (
    MaterialPolicyOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPolicyOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPolicyOutlinedIcon = MaterialPolicyOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
