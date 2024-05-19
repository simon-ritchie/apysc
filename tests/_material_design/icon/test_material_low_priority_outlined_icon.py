from apysc._material_design.icon.material_low_priority_outlined_icon import (
    MateriallowPriorityOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallowPriorityOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallowPriorityOutlinedIcon = MateriallowPriorityOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
