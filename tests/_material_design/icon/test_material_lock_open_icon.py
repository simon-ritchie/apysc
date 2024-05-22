from apysc._material_design.icon.material_lock_open_icon import MaterialLockOpenIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLockOpenIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLockOpenIcon = MaterialLockOpenIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
