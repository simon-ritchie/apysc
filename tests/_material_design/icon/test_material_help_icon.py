from apysc._material_design.icon.material_help_icon import MaterialHelpIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHelpIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHelpIcon = MaterialHelpIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
