from apysc._material_design.icon.material_lock_clock_icon import MateriallockClockIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallockClockIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallockClockIcon = MateriallockClockIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
