from apysc._material_design.icon.material_assignment_returned_icon import MaterialassignmentReturnedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialassignmentReturnedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialassignmentReturnedIcon = MaterialassignmentReturnedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
