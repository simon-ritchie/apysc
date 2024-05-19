from apysc._material_design.icon.material_rule_icon import MaterialruleIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialruleIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialruleIcon = MaterialruleIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
