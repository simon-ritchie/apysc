from apysc._material_design.icon.material_phonelink_lock_outlined_icon import (
    MaterialPhonelinkLockOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPhonelinkLockOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPhonelinkLockOutlinedIcon = MaterialPhonelinkLockOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
