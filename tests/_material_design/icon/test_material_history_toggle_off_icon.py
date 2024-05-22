from apysc._material_design.icon.material_history_toggle_off_icon import (
    MaterialHistoryToggleOffIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHistoryToggleOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHistoryToggleOffIcon = MaterialHistoryToggleOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
