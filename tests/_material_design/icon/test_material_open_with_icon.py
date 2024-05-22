from apysc._material_design.icon.material_open_with_icon import MaterialOpenWithIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOpenWithIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOpenWithIcon = MaterialOpenWithIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
