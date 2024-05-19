from apysc._material_design.icon.material_lock_outlined_icon import MateriallockOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallockOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallockOutlinedIcon = MateriallockOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
