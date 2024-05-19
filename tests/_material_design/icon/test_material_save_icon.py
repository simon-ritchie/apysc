from apysc._material_design.icon.material_save_icon import MaterialsaveIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsaveIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsaveIcon = MaterialsaveIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
