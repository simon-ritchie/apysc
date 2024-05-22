from apysc._material_design.icon.material_move_to_inbox_outlined_icon import (
    MaterialMoveToInboxOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMoveToInboxOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMoveToInboxOutlinedIcon = MaterialMoveToInboxOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
