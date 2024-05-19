from apysc._material_design.icon.material_assignment_turned_in_icon import (
    MaterialassignmentTurnedInIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialassignmentTurnedInIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialassignmentTurnedInIcon = MaterialassignmentTurnedInIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
