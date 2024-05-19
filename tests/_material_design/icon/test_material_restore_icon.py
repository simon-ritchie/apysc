from apysc._material_design.icon.material_restore_icon import MaterialrestoreIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialrestoreIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialrestoreIcon = MaterialrestoreIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
