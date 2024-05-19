from apysc._material_design.icon.material_list_alt_icon import MateriallistAltIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallistAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallistAltIcon = MateriallistAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
