from apysc._material_design.icon.material_reply_icon import MaterialreplyIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialreplyIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialreplyIcon = MaterialreplyIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
