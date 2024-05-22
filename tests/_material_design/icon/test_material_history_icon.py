from apysc._material_design.icon.material_history_icon import MaterialHistoryIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHistoryIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHistoryIcon = MaterialHistoryIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
