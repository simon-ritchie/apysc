from apysc._material_design.icon.material_sticky_note_2_icon import (
    MaterialStickyNote2Icon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialStickyNote2Icon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialStickyNote2Icon = MaterialStickyNote2Icon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
