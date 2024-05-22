from apysc._material_design.icon.material_sync_alt_icon import MaterialSyncAltIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSyncAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSyncAltIcon = MaterialSyncAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
