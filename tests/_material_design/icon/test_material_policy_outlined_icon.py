from apysc._material_design.icon.material_policy_outlined_icon import MaterialpolicyOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpolicyOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpolicyOutlinedIcon = MaterialpolicyOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
