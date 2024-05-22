from apysc._material_design.icon.material_lock_icon import MaterialLockIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLockIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLockIcon = MaterialLockIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
