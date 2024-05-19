from apysc._material_design.icon.material_note_icon import MaterialnoteIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnoteIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnoteIcon = MaterialnoteIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
