from apysc._material_design.icon.material_edit_off_icon import MaterialEditOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialEditOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialEditOffIcon = MaterialEditOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
