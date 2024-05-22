from apysc._material_design.icon.material_maximize_icon import MaterialMaximizeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMaximizeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMaximizeIcon = MaterialMaximizeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
