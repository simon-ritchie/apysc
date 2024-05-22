from apysc._material_design.icon.material_search_icon import MaterialSearchIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSearchIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSearchIcon = MaterialSearchIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
