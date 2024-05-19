from apysc._material_design.icon.material_note_add_outlined_icon import (
    MaterialnoteAddOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnoteAddOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnoteAddOutlinedIcon = MaterialnoteAddOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
