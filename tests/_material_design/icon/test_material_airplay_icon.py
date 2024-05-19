from apysc._material_design.icon.material_airplay_icon import MaterialairplayIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialairplayIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialairplayIcon = MaterialairplayIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
