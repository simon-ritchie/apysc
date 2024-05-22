from apysc._material_design.icon.material_link_off_outlined_icon import (
    MaterialLinkOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLinkOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLinkOffOutlinedIcon = MaterialLinkOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
