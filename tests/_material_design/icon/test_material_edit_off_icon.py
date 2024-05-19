from apysc._material_design.icon.material_edit_off_icon import MaterialeditOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialeditOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialeditOffIcon = MaterialeditOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
