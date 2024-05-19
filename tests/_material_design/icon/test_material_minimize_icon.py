from apysc._material_design.icon.material_minimize_icon import MaterialminimizeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialminimizeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialminimizeIcon = MaterialminimizeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
