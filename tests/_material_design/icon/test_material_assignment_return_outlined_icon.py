from apysc._material_design.icon.material_assignment_return_outlined_icon import (
    MaterialAssignmentReturnOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAssignmentReturnOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAssignmentReturnOutlinedIcon = (
            MaterialAssignmentReturnOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
