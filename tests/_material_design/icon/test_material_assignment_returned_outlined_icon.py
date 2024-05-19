from apysc._material_design.icon.material_assignment_returned_outlined_icon import MaterialassignmentReturnedOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialassignmentReturnedOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialassignmentReturnedOutlinedIcon = MaterialassignmentReturnedOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
