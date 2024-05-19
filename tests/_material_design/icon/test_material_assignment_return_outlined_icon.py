from apysc._material_design.icon.material_assignment_return_outlined_icon import (
    MaterialassignmentReturnOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialassignmentReturnOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialassignmentReturnOutlinedIcon = (
            MaterialassignmentReturnOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
