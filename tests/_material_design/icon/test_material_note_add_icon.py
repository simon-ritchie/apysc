from apysc._material_design.icon.material_note_add_icon import MaterialnoteAddIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnoteAddIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnoteAddIcon = MaterialnoteAddIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
