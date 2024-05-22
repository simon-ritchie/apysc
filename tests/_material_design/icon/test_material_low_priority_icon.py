from apysc._material_design.icon.material_low_priority_icon import (
    MaterialLowPriorityIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLowPriorityIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLowPriorityIcon = MaterialLowPriorityIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
