from apysc._material_design.icon.material_phonelink_erase_outlined_icon import (
    MaterialPhonelinkEraseOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPhonelinkEraseOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPhonelinkEraseOutlinedIcon = MaterialPhonelinkEraseOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
