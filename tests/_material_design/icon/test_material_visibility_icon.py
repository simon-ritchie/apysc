from apysc._material_design.icon.material_visibility_icon import MaterialvisibilityIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvisibilityIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvisibilityIcon = MaterialvisibilityIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
