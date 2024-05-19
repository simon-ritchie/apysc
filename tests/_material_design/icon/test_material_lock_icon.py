from apysc._material_design.icon.material_lock_icon import MateriallockIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallockIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallockIcon = MateriallockIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
