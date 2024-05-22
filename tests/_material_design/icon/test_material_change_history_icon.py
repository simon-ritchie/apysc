from apysc._material_design.icon.material_change_history_icon import (
    MaterialChangeHistoryIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialChangeHistoryIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialChangeHistoryIcon = MaterialChangeHistoryIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
