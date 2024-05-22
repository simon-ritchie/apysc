from apysc._material_design.icon.material_filter_list_alt_icon import (
    MaterialFilterListAltIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFilterListAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFilterListAltIcon = MaterialFilterListAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
