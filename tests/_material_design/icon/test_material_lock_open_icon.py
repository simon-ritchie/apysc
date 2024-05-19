from apysc._material_design.icon.material_lock_open_icon import MateriallockOpenIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallockOpenIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallockOpenIcon = MateriallockOpenIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
