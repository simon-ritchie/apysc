from apysc._material_design.icon.material_low_priority_outlined_icon import (
    MaterialLowPriorityOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLowPriorityOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLowPriorityOutlinedIcon = MaterialLowPriorityOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
