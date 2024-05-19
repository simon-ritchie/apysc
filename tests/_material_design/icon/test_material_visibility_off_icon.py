from apysc._material_design.icon.material_visibility_off_icon import MaterialvisibilityOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialvisibilityOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialvisibilityOffIcon = MaterialvisibilityOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
