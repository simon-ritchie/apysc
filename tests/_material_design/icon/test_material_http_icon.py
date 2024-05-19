from apysc._material_design.icon.material_http_icon import MaterialhttpIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhttpIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhttpIcon = MaterialhttpIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
