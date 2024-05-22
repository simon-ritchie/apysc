from apysc._material_design.icon.material_save_icon import MaterialSaveIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSaveIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSaveIcon = MaterialSaveIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
