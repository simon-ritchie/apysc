from apysc._material_design.icon.material_error_icon import MaterialerrorIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialerrorIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialerrorIcon = MaterialerrorIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
