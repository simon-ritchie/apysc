from apysc._material_design.icon.material_done_outlined_icon import (
    MaterialdoneOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdoneOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdoneOutlinedIcon = MaterialdoneOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
