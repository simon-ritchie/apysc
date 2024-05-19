from apysc._material_design.icon.material_phonelink_erase_outlined_icon import (
    MaterialphonelinkEraseOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialphonelinkEraseOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialphonelinkEraseOutlinedIcon = MaterialphonelinkEraseOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
