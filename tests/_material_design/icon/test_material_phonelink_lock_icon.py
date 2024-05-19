from apysc._material_design.icon.material_phonelink_lock_icon import MaterialphonelinkLockIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialphonelinkLockIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialphonelinkLockIcon = MaterialphonelinkLockIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
