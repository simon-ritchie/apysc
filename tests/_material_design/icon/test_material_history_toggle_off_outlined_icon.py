from apysc._material_design.icon.material_history_toggle_off_outlined_icon import (
    MaterialHistoryToggleOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHistoryToggleOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHistoryToggleOffOutlinedIcon = (
            MaterialHistoryToggleOffOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
