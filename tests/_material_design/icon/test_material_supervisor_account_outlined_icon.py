from apysc._material_design.icon.material_supervisor_account_outlined_icon import (
    MaterialSupervisorAccountOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSupervisorAccountOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSupervisorAccountOutlinedIcon = (
            MaterialSupervisorAccountOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
