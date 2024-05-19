from apysc._material_design.icon.material_phonelink_lock_outlined_icon import (
    MaterialphonelinkLockOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialphonelinkLockOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialphonelinkLockOutlinedIcon = MaterialphonelinkLockOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
