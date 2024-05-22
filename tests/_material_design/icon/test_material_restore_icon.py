from apysc._material_design.icon.material_restore_icon import MaterialRestoreIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialRestoreIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialRestoreIcon = MaterialRestoreIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
