from apysc._material_design.icon.material_assignment_returned_outlined_icon import (
    MaterialAssignmentReturnedOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAssignmentReturnedOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAssignmentReturnedOutlinedIcon = (
            MaterialAssignmentReturnedOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
