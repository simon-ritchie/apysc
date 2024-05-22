from apysc._material_design.icon.material_autorenew_icon import MaterialAutorenewIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAutorenewIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAutorenewIcon = MaterialAutorenewIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
