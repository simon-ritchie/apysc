from apysc._material_design.icon.material_assignment_ind_outlined_icon import (
    MaterialAssignmentIndOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAssignmentIndOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAssignmentIndOutlinedIcon = MaterialAssignmentIndOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
