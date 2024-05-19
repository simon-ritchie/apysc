from apysc._material_design.icon.material_link_icon import MateriallinkIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallinkIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallinkIcon = MateriallinkIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
