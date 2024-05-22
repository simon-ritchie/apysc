from apysc._material_design.icon.material_pending_actions_outlined_icon import (
    MaterialPendingActionsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPendingActionsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPendingActionsOutlinedIcon = MaterialPendingActionsOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
