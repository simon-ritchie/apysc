from apysc._material_design.icon.material_policy_icon import MaterialpolicyIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpolicyIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpolicyIcon = MaterialpolicyIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
