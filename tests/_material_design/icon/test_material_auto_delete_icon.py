from apysc._material_design.icon.material_auto_delete_icon import MaterialautoDeleteIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialautoDeleteIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialautoDeleteIcon = MaterialautoDeleteIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
