from apysc._material_design.icon.material_all_inbox_icon import MaterialAllInboxIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAllInboxIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAllInboxIcon = MaterialAllInboxIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
