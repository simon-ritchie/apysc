from apysc._material_design.icon.material_opacity_icon import MaterialOpacityIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOpacityIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOpacityIcon = MaterialOpacityIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
