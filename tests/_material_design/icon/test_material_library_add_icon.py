from apysc._material_design.icon.material_library_add_icon import MaterialLibraryAddIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLibraryAddIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLibraryAddIcon = MaterialLibraryAddIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
