from apysc._material_design.icon.material_assignment_ind_icon import (
    MaterialAssignmentIndIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAssignmentIndIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAssignmentIndIcon = MaterialAssignmentIndIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
