from apysc._material_design.icon.material_help_center_icon import MaterialhelpCenterIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhelpCenterIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhelpCenterIcon = MaterialhelpCenterIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
