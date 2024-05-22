from apysc._material_design.icon.material_supervisor_account_icon import (
    MaterialSupervisorAccountIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSupervisorAccountIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSupervisorAccountIcon = MaterialSupervisorAccountIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
