from apysc._material_design.icon.material_minimize_icon import MaterialMinimizeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMinimizeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMinimizeIcon = MaterialMinimizeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
