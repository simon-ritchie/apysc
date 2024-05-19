from apysc._material_design.icon.material_link_off_outlined_icon import MateriallinkOffOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallinkOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallinkOffOutlinedIcon = MateriallinkOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
