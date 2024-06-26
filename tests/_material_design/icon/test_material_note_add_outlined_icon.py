from apysc._material_design.icon.material_note_add_outlined_icon import (
    MaterialNoteAddOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialNoteAddOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialNoteAddOutlinedIcon = MaterialNoteAddOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
