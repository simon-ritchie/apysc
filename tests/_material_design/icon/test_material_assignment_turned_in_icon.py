from apysc._material_design.icon.material_assignment_turned_in_icon import (
    MaterialAssignmentTurnedInIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAssignmentTurnedInIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAssignmentTurnedInIcon = MaterialAssignmentTurnedInIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
