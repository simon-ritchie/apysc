from apysc._material_design.icon.material_help_center_icon import MaterialHelpCenterIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHelpCenterIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHelpCenterIcon = MaterialHelpCenterIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
