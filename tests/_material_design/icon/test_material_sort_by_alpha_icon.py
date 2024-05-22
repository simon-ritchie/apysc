from apysc._material_design.icon.material_sort_by_alpha_icon import (
    MaterialSortByAlphaIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSortByAlphaIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSortByAlphaIcon = MaterialSortByAlphaIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
