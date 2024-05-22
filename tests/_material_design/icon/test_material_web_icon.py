from apysc._material_design.icon.material_web_icon import MaterialWebIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialWebIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialWebIcon = MaterialWebIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
