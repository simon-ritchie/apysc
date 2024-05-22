from apysc._material_design.icon.material_change_history_outlined_icon import (
    MaterialChangeHistoryOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialChangeHistoryOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialChangeHistoryOutlinedIcon = MaterialChangeHistoryOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
