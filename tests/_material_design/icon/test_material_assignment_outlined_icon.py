from apysc._material_design.icon.material_assignment_outlined_icon import MaterialassignmentOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialassignmentOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialassignmentOutlinedIcon = MaterialassignmentOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
