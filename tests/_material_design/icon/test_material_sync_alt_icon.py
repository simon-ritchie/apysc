from apysc._material_design.icon.material_sync_alt_icon import MaterialsyncAltIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsyncAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsyncAltIcon = MaterialsyncAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
