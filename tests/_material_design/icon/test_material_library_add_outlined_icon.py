from apysc._material_design.icon.material_library_add_outlined_icon import MateriallibraryAddOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallibraryAddOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallibraryAddOutlinedIcon = MateriallibraryAddOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
