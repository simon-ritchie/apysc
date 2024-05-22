from apysc._material_design.icon.material_lock_open_outlined_icon import (
    MaterialLockOpenOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLockOpenOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLockOpenOutlinedIcon = MaterialLockOpenOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
