from apysc._material_design.icon.material_inbox_icon import MaterialInboxIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialInboxIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialInboxIcon = MaterialInboxIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
