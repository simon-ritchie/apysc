from apysc._material_design.icon.material_save_alt_icon import MaterialSaveAltIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSaveAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSaveAltIcon = MaterialSaveAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
