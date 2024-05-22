from apysc._material_design.icon.material_move_to_inbox_icon import (
    MaterialMoveToInboxIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMoveToInboxIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMoveToInboxIcon = MaterialMoveToInboxIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
