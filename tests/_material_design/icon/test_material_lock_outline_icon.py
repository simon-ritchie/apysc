from apysc._material_design.icon.material_lock_outline_icon import (
    MaterialLockOutlineIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLockOutlineIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLockOutlineIcon = MaterialLockOutlineIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
