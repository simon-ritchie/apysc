from apysc._material_design.icon.material_note_outlined_icon import MaterialnoteOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnoteOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnoteOutlinedIcon = MaterialnoteOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
