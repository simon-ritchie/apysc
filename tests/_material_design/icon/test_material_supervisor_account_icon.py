from apysc._material_design.icon.material_supervisor_account_icon import (
    MaterialsupervisorAccountIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsupervisorAccountIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsupervisorAccountIcon = MaterialsupervisorAccountIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
