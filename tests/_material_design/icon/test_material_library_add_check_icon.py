from apysc._material_design.icon.material_library_add_check_icon import (
    MaterialLibraryAddCheckIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLibraryAddCheckIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLibraryAddCheckIcon = MaterialLibraryAddCheckIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
