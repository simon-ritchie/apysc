from apysc._material_design.icon.material_phonelink_setup_icon import (
    MaterialPhonelinkSetupIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPhonelinkSetupIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPhonelinkSetupIcon = MaterialPhonelinkSetupIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
