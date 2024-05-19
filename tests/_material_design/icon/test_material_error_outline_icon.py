from apysc._material_design.icon.material_error_outline_icon import MaterialerrorOutlineIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialerrorOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialerrorOutlineIcon = MaterialerrorOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
