from apysc._material_design.icon.material_phonelink_setup_outlined_icon import (
    MaterialPhonelinkSetupOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPhonelinkSetupOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPhonelinkSetupOutlinedIcon = MaterialPhonelinkSetupOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
