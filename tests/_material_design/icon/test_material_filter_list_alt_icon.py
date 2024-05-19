from apysc._material_design.icon.material_filter_list_alt_icon import MaterialfilterListAltIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfilterListAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfilterListAltIcon = MaterialfilterListAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
