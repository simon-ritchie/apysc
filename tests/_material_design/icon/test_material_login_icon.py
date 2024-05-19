from apysc._material_design.icon.material_login_icon import MaterialloginIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialloginIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialloginIcon = MaterialloginIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
