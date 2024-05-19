from apysc._material_design.icon.material_autorenew_icon import MaterialautorenewIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialautorenewIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialautorenewIcon = MaterialautorenewIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
