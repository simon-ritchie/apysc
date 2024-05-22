from apysc._material_design.icon.material_assignment_late_outlined_icon import (
    MaterialAssignmentLateOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAssignmentLateOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAssignmentLateOutlinedIcon = MaterialAssignmentLateOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
