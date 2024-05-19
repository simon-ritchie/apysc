from apysc._material_design.icon.material_move_to_inbox_icon import MaterialmoveToInboxIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmoveToInboxIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmoveToInboxIcon = MaterialmoveToInboxIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
