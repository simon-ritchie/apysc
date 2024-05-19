from apysc._material_design.icon.material_all_inbox_icon import MaterialallInboxIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialallInboxIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialallInboxIcon = MaterialallInboxIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
