from apysc._material_design.icon.material_phonelink_erase_icon import (
    MaterialPhonelinkEraseIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPhonelinkEraseIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPhonelinkEraseIcon = MaterialPhonelinkEraseIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
