from apysc._material_design.icon.material_search_icon import MaterialsearchIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsearchIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsearchIcon = MaterialsearchIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
