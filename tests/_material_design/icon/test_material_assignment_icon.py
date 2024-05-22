from apysc._material_design.icon.material_assignment_icon import MaterialAssignmentIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAssignmentIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAssignmentIcon = MaterialAssignmentIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
