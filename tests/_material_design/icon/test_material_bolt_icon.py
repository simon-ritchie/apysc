from apysc._material_design.icon.material_bolt_icon import MaterialboltIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialboltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialboltIcon = MaterialboltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
