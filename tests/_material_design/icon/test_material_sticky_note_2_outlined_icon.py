from apysc._material_design.icon.material_sticky_note_2_outlined_icon import (
    MaterialStickyNote2OutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialStickyNote2OutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialStickyNote2OutlinedIcon = MaterialStickyNote2OutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
