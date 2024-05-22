from apysc._material_design.icon.material_anchor_outlined_icon import (
    MaterialAnchorOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAnchorOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAnchorOutlinedIcon = MaterialAnchorOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
