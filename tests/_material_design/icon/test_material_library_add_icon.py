from apysc._material_design.icon.material_library_add_icon import MateriallibraryAddIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallibraryAddIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallibraryAddIcon = MateriallibraryAddIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
