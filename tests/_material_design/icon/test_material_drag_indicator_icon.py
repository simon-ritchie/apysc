from apysc._material_design.icon.material_drag_indicator_icon import (
    MaterialDragIndicatorIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialDragIndicatorIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialDragIndicatorIcon = MaterialDragIndicatorIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
