from apysc._material_design.icon.material_list_alt_icon import MaterialListAltIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialListAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialListAltIcon = MaterialListAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
