from apysc._material_design.icon.material_assignment_ind_outlined_icon import MaterialassignmentIndOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialassignmentIndOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialassignmentIndOutlinedIcon = MaterialassignmentIndOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
