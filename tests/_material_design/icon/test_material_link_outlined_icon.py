from apysc._material_design.icon.material_link_outlined_icon import (
    MaterialLinkOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLinkOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLinkOutlinedIcon = MaterialLinkOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
