from apysc._material_design.icon.material_saved_search_icon import (
    MaterialSavedSearchIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSavedSearchIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSavedSearchIcon = MaterialSavedSearchIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
