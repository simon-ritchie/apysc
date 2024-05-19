from apysc._material_design.icon.material_link_off_icon import MateriallinkOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallinkOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallinkOffIcon = MateriallinkOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
