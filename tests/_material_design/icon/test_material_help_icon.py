from apysc._material_design.icon.material_help_icon import MaterialhelpIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhelpIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhelpIcon = MaterialhelpIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
