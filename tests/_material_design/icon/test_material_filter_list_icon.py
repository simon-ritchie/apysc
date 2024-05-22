from apysc._material_design.icon.material_filter_list_icon import MaterialFilterListIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFilterListIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFilterListIcon = MaterialFilterListIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
