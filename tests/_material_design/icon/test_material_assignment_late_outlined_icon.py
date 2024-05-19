from apysc._material_design.icon.material_assignment_late_outlined_icon import (
    MaterialassignmentLateOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialassignmentLateOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialassignmentLateOutlinedIcon = MaterialassignmentLateOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
