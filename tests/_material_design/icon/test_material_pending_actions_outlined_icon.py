from apysc._material_design.icon.material_pending_actions_outlined_icon import (
    MaterialpendingActionsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpendingActionsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpendingActionsOutlinedIcon = MaterialpendingActionsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
