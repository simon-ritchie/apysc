from apysc._material_design.icon.material_reply_all_icon import MaterialreplyAllIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialreplyAllIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialreplyAllIcon = MaterialreplyAllIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
