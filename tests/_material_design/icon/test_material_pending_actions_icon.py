from apysc._material_design.icon.material_pending_actions_icon import (
    MaterialpendingActionsIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpendingActionsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpendingActionsIcon = MaterialpendingActionsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
